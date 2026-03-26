# DevOps

## Config

| Key            | Value          | Description                                 |
|----------------|----------------|---------------------------------------------|
| ci_provider    | github-actions | CI provider                                 |
| trigger_branch | master         | Default branch for triggers                 |
| diff_range     | HEAD~5         | Git diff range for auto-analysis in feature |

## Rules

### Workflow Registry

| Workflow | File                            | Trigger         | Purpose             |
|----------|---------------------------------|-----------------|---------------------|
| Lint     | `.github/workflows/lint.yml`    | push/PR to master | ruff check + format |
| Tests    | `.github/workflows/tests.yml`   | push/PR to master | pytest matrix       |
| Docs     | `.github/workflows/docs.yml`    | push/PR to master | mkdocs build        |
| Publish  | `.github/workflows/publish.yml` | tag v*          | PyPI release (token auth) |

### Conventions