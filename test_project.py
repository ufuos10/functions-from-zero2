from mylib.calc import *
from calCLI import cli
from click.testing import CliRunner
import pytest


@pytest.fixture
def runner():
    return CliRunner()


# Write a test for each command in calCLI.py
def test_cli_add(runner):
    result = runner.invoke(cli, ["add", "1", "2"])
    assert result.exit_code == 0
    assert "The sum of 1.0 and 2.0 is: 3.0" in result.output


def test_cli_subtract(runner):
    result = runner.invoke(cli, ["subtract", "5", "3"])
    assert result.exit_code == 0
    assert "The difference of 5.0 and 3.0 is: 2.0" in result.output


def test_cli_multiply(runner):
    result = runner.invoke(cli, ["multiply", "4", "5"])
    assert result.exit_code == 0
    assert "The product of 4.0 and 5.0 is: 20.0" in result.output


def test_cli_divide(runner):
    result = runner.invoke(cli, ["divide", "10", "2"])
    assert result.exit_code == 0
    assert "The quotient of 10.0 and 2.0 is: 5.0" in result.output

    result = runner.invoke(cli, ["divide", "5", "0"])
    assert result.exit_code == 0
    assert "Cannot divide by zero." in result.output


def test_cli_power(runner):
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert "2.0 raised to the power of 3.0 is: 8.0" in result.output


def test_help(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert (
        "A calculator program that provides basic arithmetic operations."
        in result.output
    )


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, -3) == 2
    assert divide(0, 1) == 0

    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8
