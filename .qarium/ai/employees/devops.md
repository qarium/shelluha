# DevOps

## Config

| Key            | Value          | Description                                 |
|----------------|----------------|---------------------------------------------|
| ci_provider    | github-actions | CI provider                                 |
| trigger_branch | 0.0.x          | Default branch for triggers                 |
| diff_range     | HEAD~5         | Git diff range for auto-analysis in feature |

## Rules

### Workflow Registry

| Workflow | File                            | Trigger               | Purpose             |
|----------|---------------------------------|-----------------------|---------------------|
| Lint     | `.github/workflows/lint.yml`    | push/PR to 0.0.x      | ruff check + format |
| Tests    | `.github/workflows/tests.yml`   | push/PR to 0.0.x      | pytest matrix       |
| Docs     | `.github/workflows/docs.yml`    | push to 0.0.x         | mkdocs gh-deploy    |
| Strictacode | `.github/workflows/strictacode.yml` | push/PR to 0.0.x | code quality analysis |
| Publish  | `.github/workflows/publish.yml` | workflow_dispatch     | PyPI release + GitHub Release |
| New Version | `.github/workflows/new_version.yml` | workflow_dispatch | create version branch |

### Conventions

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|