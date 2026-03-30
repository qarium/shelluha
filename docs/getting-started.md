# Getting Started

## Installation

Install shelluha using pip:

```bash
pip install shelluha
```

## Basic Usage

### Execute a Command

Use `shell.shell_exec()` to run shell commands:

```python
from shelluha import shell

# Simple command
output = shell.shell_exec("ls -la")
print(output)

# With sudo
output = shell.shell_exec("apt update", is_sudo=True)

# Auto-confirm prompts
output = shell.shell_exec("rm -rf dir", yes=True)

# Provide input to prompts
output = shell.shell_exec("ssh-keygen", prompt_input=["", "", ""])
```

### Create Reusable Commands

Use `ShellCommand` to wrap frequently used binaries:

```python
from shelluha import ShellCommand

docker = ShellCommand("docker")

# Call with options
docker("ps -a")
docker("images")

# Access the binary name
print(docker.bin)  # "docker"
```

### Temporary Directory Change

Use `shell.cd()` as a context manager:

```python
from shelluha import shell

with shell.cd("/tmp"):
    # Working directory is now /tmp
    shell.shell_exec("pwd")  # /tmp

# Working directory is restored
shell.shell_exec("pwd")  # original directory
```

### Error Handling

Commands that fail raise `ShellExecError`:

```python
from shelluha import shell

try:
    shell.shell_exec("exit 1")
except shell.ShellExecError as e:
    print(f"Command failed: {e}")
```

## Pre-initialized Commands

The following commands are available out of the box:

```python
from shelluha import shell

shell.ps("-aux")
shell.df("-h")
shell.du("-sh /home")
```