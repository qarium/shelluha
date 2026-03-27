# Tech Writer Config

## Config

| Key           | Value                                                    | Description                         |
|---------------|----------------------------------------------------------|-------------------------------------|
| build_cmd     | `mkdocs build`                                           | Build validation command            |
| deploy_cmd    | `mkdocs gh-deploy --force`                               | Deploy command                      |
| examples_file | `docs/examples.md`                                       | File for usage examples             |
| logo_url      | `https://avatars.githubusercontent.com/u/262344922?s=200&v=4` | Standard qarium logo           |
| base_branch   | `master`                                                 | Base branch for git diff comparison |

## Rules

### Mapping

| Source path            | Documentation files                                              |
|------------------------|------------------------------------------------------------------|
| `shelluha/shell.py`    | `docs/api-reference.md`, `docs/getting-started.md`, `docs/index.md` |
| `shelluha/__init__.py` | `docs/api-reference.md`                                          |

### Conventions

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|