"""Exercise portable copying and meaningful validator/activation failures."""
from pathlib import Path
import hashlib
import importlib.util
import json
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


checker = module(ROOT / '.agents/scripts/validate.py', 'toolkit_validator')
activator = module(ROOT / '.agents/scripts/activate.py', 'toolkit_activator')
errors, count = checker.validate(ROOT / '.agents', ROOT)
assert not errors and count == 41, errors
print('PASS: active author-grouped toolkit, 41 skills, explicit policies, catalog, workflow paths.')

revision = '49dd158d1076134a641b33efb035946536778336'
source = ROOT / 'skill-selection/downloads' / ('mattpocock-' + revision) / ('skills-' + revision)
inventory = json.loads((ROOT / '.agents/IMPORTS.json').read_text(encoding='utf-8'))
checked = 0
for record in inventory['imports']:
    for resource in record['files']:
        if resource['source_path'] is None:
            continue
        original = source / resource['source_path']
        assert hashlib.sha256(original.read_bytes()).hexdigest() == resource['upstream_sha256']
        installed = ROOT / '.agents' / resource['path']
        assert hashlib.sha256(installed.read_bytes()).hexdigest() == resource['installed_sha256']
        if installed.suffix in ('.sh', '.cjs'):
            assert installed.read_bytes() == original.read_bytes()
        checked += 1
assert checked == 103
print('PASS: all 103 upstream resources accounted for; executable/config templates unchanged.')

with tempfile.TemporaryDirectory(prefix='patompong-portability-') as temporary:
    project = Path(temporary) / 'another-project'
    project.mkdir()
    toolkit = project / '.agents'
    shutil.copytree(ROOT / '.agents', toolkit)
    existing = b'# Existing project rules\r\n\r\nPreserve this project-specific guidance.\r\n'
    (project / 'AGENTS.md').write_bytes(existing)
    result = activator.activate(project, toolkit)
    assert 'appended' in result
    first = (project / 'AGENTS.md').read_bytes()
    assert first.startswith(existing)
    assert activator.activate(project, toolkit) == 'Already activated; no files changed.'
    assert first == (project / 'AGENTS.md').read_bytes()
    errors, copied_count = checker.validate(toolkit, project)
    assert not errors and copied_count == 41, errors
    print('PASS: copied toolkit validates; activation preserves existing guidance and is idempotent.')

    def expect_failure(label, mutate, restore, expected):
        mutate()
        failures, _ = checker.validate(toolkit, project)
        assert any(expected in error for error in failures), (label, failures)
        restore()
        print('PASS: validator rejects ' + label + '.')

    policy = toolkit / 'skills/mattpocock/grill-me/agents/openai.yaml'
    saved = policy.read_bytes()
    expect_failure('accidental implicit invocation',
                   lambda: policy.write_bytes(saved.replace(b'allow_implicit_invocation: false', b'allow_implicit_invocation: true')),
                   lambda: policy.write_bytes(saved), 'Expected explicit-only policy')

    reference = toolkit / 'skills/mattpocock/codebase-design/DEEPENING.md'
    saved = reference.read_bytes()
    expect_failure('missing bundled reference', reference.unlink,
                   lambda: reference.write_bytes(saved), 'Missing imported resource')

    workflow = toolkit / 'workflows/interview.md'
    saved = workflow.read_bytes()
    expect_failure('broken workflow skill entry',
                   lambda: workflow.write_bytes(saved + b'\nRead `.agents/skills/mattpocock/nonexistent/SKILL.md`.\n'),
                   lambda: workflow.write_bytes(saved), 'Broken skill entry path')

    manifest = toolkit / 'skills/mattpocock/grill-me/SKILL.md'
    saved = manifest.read_bytes()
    expect_failure('missing grouped manifest', manifest.unlink,
                   lambda: manifest.write_bytes(saved), 'Missing grouped skill manifest')

    saved = reference.read_bytes()
    expect_failure('unrecorded imported-file changes',
                   lambda: reference.write_bytes(saved + b'\nUnrecorded edit.\n'),
                   lambda: reference.write_bytes(saved), 'Unrecorded imported resource change')

    saved = workflow.read_bytes()
    expect_failure('a real broken Markdown link',
                   lambda: workflow.write_bytes(saved + b'\n[Missing](../missing-resource.md)\n'),
                   lambda: workflow.write_bytes(saved), 'Broken link')

    (project / 'AGENTS.override.md').write_text('# Override\n', encoding='utf-8')
    try:
        activator.activate(project, toolkit)
    except ValueError as error:
        assert 'override' in str(error)
    else:
        raise AssertionError('Activation must reject a conflicting override')
    (project / 'AGENTS.override.md').unlink()
    print('PASS: activation refuses a conflicting root override.')
    errors, _ = checker.validate(toolkit, project)
    assert not errors, errors

print('PASS: portable packaging and failure-path checks complete. Host session behavior is not runtime-tested.')
