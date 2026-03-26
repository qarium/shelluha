# Lead

## Architecture & Decisions
- **ShellCommand wrapper class** — encapsulates binary path and delegates to `shell_exec()`, enabling reusable command objects like `ps()`, `df()`
- **shell_exec() as core primitive** — single function handles all subprocess execution with consistent error handling via `ShellExecError`
- **cd() as context manager** — temporary directory changes with automatic restoration using try/finally
- **setuptools-scm for dynamic versioning** — version derived from git tags via pyproject.toml, eliminates manual version management
- **ruff as unified linter/formatter** — replaces black/isort/flake8, configured with rules E, W, F, I, UP, B, SIM, C4, DTZ, PT
- **PyPI trusted publishing via OIDC** — publish.yml uses pypa/gh-action-pypi-publish with id-token: write, no API tokens needed

## Project Structure
- **Single module shelluha/shell.py** — all shell utilities in one file, not split into submodules
- **Pre-initialized commands at module level** — instances like `ps`, `df`, `du` created at import time for immediate use
- **Tests mirror source structure** — `tests/test_shell/` corresponds to `shelluha/shell.py`
- **CI workflows in .github/workflows/** — lint.yml (ruff), tests.yml (matrix 3.10-3.13), publish.yml (tag-triggered)

## Code Patterns
- **typing as t alias** — `import typing as t` used throughout for type hints
- **ShellExecError on non-zero exit codes** — subprocess failures raise custom exception with command and stderr in message
- **pytest + hamcrest matchers** — tests use `import hamcrest as h` with assertions like `h.assert_that(...)`
- **Mock patches as module-level decorators** — common pattern: `mock_popen = mock.patch(...)` then `@mock_popen def test_...`
- **Pylint inline suppressions** — `# pylint: disable=...` used for intentional style deviations
- **# type: ignore[specific-rule]** — targeted mypy suppressions (e.g., `# type: ignore[str-bytes-safe]`), not broad ignores
- **autospec= in mock.patch** — enforces real function signatures in tests

## TODO
<!-- empty -->

## LLM Directives
<!-- empty -->