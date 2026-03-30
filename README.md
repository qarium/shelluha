# shelluha

Shell command execution utilities for Python.

## Installation

```bash
pip install shelluha
```

## Quick Start

```python
from shelluha import shell, ShellCommand

# Execute a command
output = shell.shell_exec("ls -la")

# Create a reusable command
docker = ShellCommand("docker")
docker("ps")

# Temporary directory change
with shell.cd("/tmp"):
    shell.shell_exec("pwd")
```

## Documentation

Full documentation is available at [https://qarium.github.io/shelluha/](https://qarium.github.io/shelluha/)