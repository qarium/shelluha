## Config

| Setting          | Value                                  |
|------------------|----------------------------------------|
| run_tests_cmd    | `pytest --tb=short`                    |
| lint_cmd         | `ruff check shelluha/ tests/`          |
| lint_fix_cmd     | `ruff check --fix shelluha/ tests/`    |
| format_cmd       | `ruff format --check shelluha/ tests/` |
| format_fix_cmd   | `ruff format shelluha/ tests/`         |

## Rules

Project test configuration. Used by the `qarium:employees:qa:feature` skill.

### Mapping

| Source path pattern | Test directory      | Notes         |
|---------------------|---------------------|---------------|
| `shelluha/**/*.py`  | `tests/test_shell/` | Mirror layout |

### Mock Patterns

| Pattern | Example |
|---------|---------|

### Helpers

| Helper | Location | Purpose |
|--------|----------|---------|

### Conventions

- Naming: `test_<what>_<scenario>`
- Never mock `builtins.open` — use `tmp_path` fixture
- Integration tests use `pytest.mark.skipif` when external tools unavailable

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|