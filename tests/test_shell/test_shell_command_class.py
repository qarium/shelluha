from unittest import mock

import hamcrest as h
import shelluha
from shelluha.shell import ShellCommand

shell_exec_func_mock = mock.patch(
    "shelluha.shell.shell_exec", autospec=shelluha.shell.shell_exec, return_value="test_pass"
)


@shell_exec_func_mock
def test_shell_command_class_call_to_shell_exec_func(_: mock.MagicMock) -> None:
    command = ShellCommand("ps")
    h.assert_that(command(), h.equal_to("test_pass"))


# pylint: disable=W0212
def test_shell_command_class_bin_file() -> None:
    command = ShellCommand("ps")
    h.assert_that(command._bin_file, h.equal_to("ps"))


@shell_exec_func_mock
def test_shell_command_class_arguments(shell_exec_mock: mock.MagicMock) -> None:
    command = ShellCommand("ps")
    command(*["-option1", "--option2"], **{"env": "value"})

    args, kwargs = shell_exec_mock.call_args

    h.assert_that(args, h.equal_to(("ps -option1 --option2",)))
    h.assert_that(kwargs, h.equal_to({"env": "value"}))


def test_shell_command_bin_property() -> None:
    command = ShellCommand("ls")
    h.assert_that(command.bin, h.equal_to("ls"))
