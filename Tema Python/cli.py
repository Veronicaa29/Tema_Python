import click
import threading
from math_ops import factorial, fibonacci, power
from models import FactorialInput, FibonacciInput, PowerInput
from database import init_db, save_request


init_db()


@click.group()
def cli():
    """CLI for simple mathematical operations"""
    pass


@cli.command()
@click.option('--base', type=float, required=True)
@click.option('--exp', type=float, required=True)
def pow(base, exp):
    """Raises a number to a power"""
    data = PowerInput(base=base, exp=exp)
    def worker():
        result = power(data.base, data.exp)
        click.echo(f"Result is: {result}")
        save_request("power", data.model_dump_json(), str(result))
    t = threading.Thread(target=worker)
    t.start()
    t.join()


@cli.command()
@click.option('--number', type=int, required=True)
def factorial_cmd(number):
    """Calculates the factorial of a number"""
    data = FactorialInput(number=number)
    def worker():
        result = factorial(data.number)
        click.echo(f"Factorial is: {result}")
        save_request("factorial", data.model_dump_json(), str(result))
    t = threading.Thread(target=worker)
    t.start()
    t.join()


@cli.command()
@click.option('--number', type=int, required=True)
def fib(number):
    """Calculates the n-th Fibonacci number"""
    data = FibonacciInput(number=number)
    def worker():
        result = fibonacci(data.number)
        click.echo(f"Fibonacci number is: {result}")
        save_request("fibonacci", data.model_dump_json(), str(result))
    t = threading.Thread(target=worker)
    t.start()
    t.join()


if __name__ == '__main__':
    cli()
