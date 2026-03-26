import logging
import os
import typing as t
from contextlib import contextmanager
from subprocess import PIPE, Popen

logger = logging.getLogger(__name__)


# pylint: disable=invalid-name
@contextmanager
def cd(path: str) -> t.Generator:
    current_path = os.getcwd()

    try:
        logger.debug(f'change working from "{current_path}" to "{path}"')
        os.chdir(path)
        yield
    finally:
        logger.debug(f'restore working dir from "{path}" to "{current_path}"')
        os.chdir(current_path)


class ShellExecError(Exception):
    pass


def shell_exec(
    cmd: str,
    *,
    env: t.Any = None,
    cwd: t.Optional[str | bytes | os.PathLike[str] | os.PathLike[bytes]] = None,
    stdin: t.Optional[int] = None,
    stdout: int = PIPE,
    stderr: int = PIPE,
    yes: bool = False,
    is_sudo: bool = False,
    prompt_input: t.Optional[str | list[str]] = None,
) -> t.Optional[str]:
    logger.debug(f'execute shell command "{cmd}"')  # type: ignore[str-bytes-safe]
    if is_sudo:
        cmd = f"sudo {cmd}"

    if yes:
        cmd = f"yes | {cmd}"

    if prompt_input:
        if isinstance(prompt_input, list):
            prompt_input = "\n".join(prompt_input)
        prompt_input = prompt_input + "\n"
        prompt_input = prompt_input.encode()  # type: ignore[assignment]

    # # pylint: disable=R1732
    process = Popen(cmd, env=env, cwd=cwd, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)

    result, error = process.communicate(input=prompt_input)  # type: ignore[arg-type]

    if result is not None:
        result = result.decode("utf-8")  # type: ignore[assignment]
    if error is not None:
        error = error.decode("utf-8")  # type: ignore[assignment]

    code = process.poll()

    if code != 0:
        raise ShellExecError(f"{cmd}\n{error}" if error else f"{cmd}")  # type: ignore[str-bytes-safe]

    return result  # type: ignore[return-value]


class ShellCommand:
    def __init__(self, bin_file: str):
        self._bin_file = bin_file

    def __call__(self, *options: str, **kwargs: t.Any) -> t.Optional[str]:
        return shell_exec(f"{self._bin_file} {' '.join(options)}", **kwargs)

    @property
    def bin(self) -> str:
        return self._bin_file


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
