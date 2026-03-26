# API Reference

## Functions

### `shell_exec()`

Execute a shell command and return its output.

```python
def shell_exec(
    cmd: str,
    *,
    env: Any = None,
    cwd: str | bytes | os.PathLike | None = None,
    stdin: int | None = None,
    stdout: int = PIPE,
    stderr: int = PIPE,
    yes: bool = False,
    is_sudo: bool = False,
    prompt_input: str | list[str] | None = None,
) -> str | None:
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `cmd` | `str` | required | Shell command to execute |
| `env` | `Any` | `None` | Environment variables dict |
| `cwd` | `str \| bytes \| os.PathLike \| None` | `None` | Working directory |
| `stdin` | `int \| None` | `None` | stdin file descriptor |
| `stdout` | `int` | `PIPE` | stdout file descriptor |
| `stderr` | `int` | `PIPE` | stderr file descriptor |
| `yes` | `bool` | `False` | Pipe `yes` to command input |
| `is_sudo` | `bool` | `False` | Prefix command with `sudo` |
| `prompt_input` | `str \| list[str] \| None` | `None` | Input to send to stdin |

**Returns:** `str | None` — Command stdout, or `None` if empty.

**Raises:** `ShellExecError` — If command exits with non-zero code.

**Example:**

```python
from shelluha.shell import shell_exec

output = shell_exec("ls -la", cwd="/tmp")
```

---

### `cd()`

Context manager for temporary directory changes.

```python
@contextmanager
def cd(path: str) -> Generator:
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `path` | `str` | Directory path to change to |

**Example:**

```python
from shelluha.shell import cd

with cd("/tmp"):
    # Working directory is /tmp
    pass
# Working directory restored
```

---

## Classes

### `ShellCommand`

Wrapper class for shell commands.

```python
class ShellCommand:
    def __init__(self, bin_file: str) -> None: ...
    def __call__(self, *options: str, **kwargs: Any) -> str | None: ...
    @property
    def bin(self) -> str: ...
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `bin_file` | `str` | Binary name or path |

**Methods:**

| Method | Returns | Description |
|--------|---------|-------------|
| `__call__(*options, **kwargs)` | `str \| None` | Execute command with options |
| `bin` | `str` | Get the binary name |

**Example:**

```python
from shelluha.shell import ShellCommand

git = ShellCommand("git")
git("status")
print(git.bin)  # "git"
```

---

## Exceptions

### `ShellExecError`

Raised when a shell command exits with a non-zero code.

```python
class ShellExecError(Exception):
    pass
```

**Message format:** `<command>\n<stderr>` (stderr included if available)

**Example:**

```python
from shelluha.shell import shell_exec, ShellExecError

try:
    shell_exec("false")
except ShellExecError as e:
    print(e)  # "false\n" or "false" if no stderr
```

---

## Pre-initialized Commands

The module provides pre-initialized `ShellCommand` instances:

```python
ps = ShellCommand("ps")
df = ShellCommand("df")
du = ShellCommand("du")
cat = ShellCommand("cat")
tar = ShellCommand("tar")
tail = ShellCommand("tail")
head = ShellCommand("head")
touch = ShellCommand("touch")
chown = ShellCommand("chown")
chmod = ShellCommand("chmod")
chgrp = ShellCommand("chgrp")
which = ShellCommand("which")
```