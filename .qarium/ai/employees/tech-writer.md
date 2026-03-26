# Tech Writer Config

## Config

| Key           | Value                      | Description                        |
|---------------|----------------------------|------------------------------------|
| build_cmd     | `mkdocs build`             | Build validation command           |
| deploy_cmd    | `mkdocs gh-deploy --force` | Deploy command                     |
| examples_file |                            | File for usage examples (optional) |
| logo_url      |                            | Header logo URL (optional)         |

## Rules

### Mapping

| Source path            | Documentation files                                         |
|------------------------|-------------------------------------------------------------|
| `shelluha/shell.py`    | `docs/api-reference.md`, `docs/getting-started.md`, `docs/index.md` |
| `shelluha/__init__.py` | `docs/api-reference.md`                                     |

### Conventions