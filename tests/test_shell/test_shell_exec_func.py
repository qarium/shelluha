from unittest import mock

import hamcrest as h
import shelluha
from shelluha.shell import ShellExecError, shell_exec

mock_communicate = mock.MagicMock(return_value=(b"output_pass", b"error"))

mock_popen_with_communicate_func_mock = mock.patch(
    "shelluha.shell.Popen",
    autospec=shelluha.shell.Popen,
    return_value=mock.MagicMock(**{"communicate.side_effect": mock_communicate, "poll.side_effect": lambda: 0}),
)

mock_popen_with_error_code = mock.patch(
    "shelluha.shell.Popen",
    autospec=shelluha.shell.Popen,
    return_value=mock.MagicMock(
        spec_set=["communicate", "poll"],
        **{"communicate.return_value": (b"output_pass", b"error"), "poll.return_value": 1},
    ),
)


@mock_popen_with_communicate_func_mock
def test_shell_exec_func_call_to_popen_object(mock_popen: mock.MagicMock) -> None:
    shell_exec("ps")
    h.assert_that(mock_popen.called, h.equal_to(True))


@mock_popen_with_communicate_func_mock
def test_shell_exec_func_return_value_positive(_: mock.MagicMock) -> None:
    h.assert_that(shell_exec("ps"), h.equal_to("output_pass"))


@mock_popen_with_error_code
def test_shell_exec_func_catch_exception(_: mock.MagicMock) -> None:
    h.assert_that(h.calling(shell_exec).with_args("ps"), h.raises(ShellExecError))


@mock_popen_with_communicate_func_mock
def test_shell_exec_func_call_check_call_args_sudo_true(mock_popen: mock.MagicMock) -> None:
    shell_exec("ps", env="test", cwd="cwd", stdin=1, stdout=2, stderr=3, is_sudo=True)
    args, kwargs = mock_popen.call_args
    h.assert_that(args, h.equal_to(("sudo ps",)))
    h.assert_that(
        kwargs, h.equal_to({"env": "test", "cwd": "cwd", "shell": True, "stdin": 1, "stdout": 2, "stderr": 3})
    )


@mock_popen_with_communicate_func_mock
def test_shell_exec_func_call_check_call_args_sudo_false(mock_popen: mock.MagicMock) -> None:
    shell_exec("ps", is_sudo=False)
    args, _ = mock_popen.call_args
    h.assert_that(args, h.equal_to(("ps",)))


@mock_popen_with_communicate_func_mock
def test_shell_exec_func_with_communicate_func_mock_string(_: mock.MagicMock) -> None:
    shell_exec("ps", prompt_input="test_pass")

    _, kwargs = mock_communicate.call_args

    h.assert_that(mock_communicate.called, h.equal_to(True))
    h.assert_that(kwargs.get("input").decode("utf-8"), h.equal_to("test_pass\n"))


@mock_popen_with_communicate_func_mock
def test_shell_exec_func_with_communicate_func_mock_list(_: mock.MagicMock) -> None:
    shell_exec("ps", prompt_input=["test_pass_1", "test_pass_2"])

    _, kwargs = mock_communicate.call_args

    h.assert_that(mock_communicate.called, h.equal_to(True))
    h.assert_that(kwargs.get("input").decode("utf-8"), h.equal_to("test_pass_1\ntest_pass_2\n"))


@mock_popen_with_communicate_func_mock
def test_shell_exec_func_yes_flag(mock_popen: mock.MagicMock) -> None:
    shell_exec("rm", yes=True)
    args, _ = mock_popen.call_args
    h.assert_that(args, h.equal_to(("yes | rm",)))


mock_popen_with_error_and_stderr = mock.patch(
    "shelluha.shell.Popen",
    autospec=shelluha.shell.Popen,
    return_value=mock.MagicMock(
        spec_set=["communicate", "poll"],
        **{"communicate.return_value": (b"output", b"error message"), "poll.return_value": 1},
    ),
)


@mock_popen_with_error_and_stderr
def test_shell_exec_func_error_includes_stderr(_: mock.MagicMock) -> None:
    h.assert_that(h.calling(shell_exec).with_args("fail"), h.raises(ShellExecError))
    try:
        shell_exec("fail")
    except ShellExecError as e:
        h.assert_that(str(e), h.contains_string("error message"))
