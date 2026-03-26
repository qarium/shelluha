# shelluha

Shell command execution utilities for Python.

## Features

- **`shell_exec()`** — Execute shell commands with consistent error handling
- **`ShellCommand`** — Create reusable command wrappers
- **`cd()`** — Context manager for temporary directory changes
- Pre-initialized commands: `ps`, `df`, `du`, `cat`, `tar`, `tail`, `head`, `touch`, `chown`, `chmod`, `chgrp`, `which`

## Installation

```bash
pip install shelluha
```

## Quick Start

```python
from shelluha.shell import shell_exec, ShellCommand, cd

# Execute a command
output = shell_exec("ls -la")

# Create a reusable command
docker = ShellCommand("docker")
docker("ps")

# Temporary directory change
with cd("/tmp"):
    shell_exec("pwd")
```

## Documentation

- [Getting Started](getting-started.md) — Installation and basic usage
- [API Reference](api-reference.md) — Complete API documentation