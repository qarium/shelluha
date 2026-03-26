# shelluha

Shell command execution utilities for Python.

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

Full documentation is available at [https://qarium.github.io/shelluha/](https://qarium.github.io/shelluha/)