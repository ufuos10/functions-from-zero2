#!/usr/bin/env python
import click

from mylib.calc import add, subtract, multiply, divide, power


@click.group()
def cli():
    """A calculator program that provides basic arithmetic operations."""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers.

    Example: ./calCLI.py add 1 2
    """
    result = add(a, b)
    click.secho(f"The sum of {a} and {b} is: {result}", fg="green")


@cli.command("subtract")
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_command(a, b):
    """Subtract two numbers.

    Example: ./calCLI.py subtract 5 3
    """
    result = subtract(a, b)
    click.secho(f"The difference of {a} and {b} is: {result}", fg="yellow")


@cli.command("multiply")
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_command(a, b):
    """Multiply two numbers.

    Example: ./calCLI.py multiply 4 5
    """
    result = multiply(a, b)
    click.secho(f"The product of {a} and {b} is: {result}", fg="blue")


@cli.command("divide")
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_command(a, b):
    """Divide two numbers.

    Example: ./calCLI.py divide 10 2
    """
    try:
        result = divide(a, b)
        click.secho(f"The quotient of {a} and {b} is: {result}", fg="red")
    except ValueError as e:
        click.secho(str(e), fg="red")


@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_command(a, b):
    """Raise a to the power of b.

    Example: ./calCLI.py power 2 3
    """
    result = power(a, b)
    click.secho(f"{a} raised to the power of {b} is: {result}", fg="magenta")


if __name__ == "__main__":
    cli()
