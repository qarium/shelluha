# Getting Started

## Installation

Install shelluha using pip:

```bash
pip install shelluha
```

## Basic Usage

### Execute a Command

Use `shell_exec()` to run shell commands:

```python
from shelluha.shell import shell_exec

# Simple command
output = shell_exec("ls -la")
print(output)

# With sudo
output = shell_exec("apt update", is_sudo=True)

# Auto-confirm prompts
output = shell_exec("rm -rf dir", yes=True)

# Provide input to prompts
output = shell_exec("ssh-keygen", prompt_input=["", "", ""])
```

### Create Reusable Commands

Use `ShellCommand` to wrap frequently used binaries:

```python
from shelluha.shell import ShellCommand

docker = ShellCommand("docker")

# Call with options
docker("ps -a")
docker("images")

# Access the binary name
print(docker.bin)  # "docker"
```

### Temporary Directory Change

Use `cd()` as a context manager:

```python
from shelluha.shell import cd

with cd("/tmp"):
    # Working directory is now /tmp
    shell_exec("pwd")  # /tmp

# Working directory is restored
shell_exec("pwd")  # original directory
```

### Error Handling

Commands that fail raise `ShellExecError`:

```python
from shelluha.shell import shell_exec, ShellExecError

try:
    shell_exec("exit 1")
except ShellExecError as e:
    print(f"Command failed: {e}")
```

## Pre-initialized Commands

The following commands are available out of the box:

```python
from shelluha.shell import ps, df, du, cat, tar, tail, head, touch, chown, chmod, chgrp, which

ps("-aux")
df("-h")
du("-sh /home")
```