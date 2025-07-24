import click
import threading
from math_ops import factorial, fibonacci, power
from models import FactorialInput, FibonacciInput, PowerInput
from database import init_db, save_request


init_db()


@click.group()
def cli():
    """CLI pentru operații matematice simple"""
    pass


@cli.command()
@click.option('--base', type=float, required=True)
@click.option('--exp', type=float, required=True)
def pow(base, exp):
    """Ridică un număr la o putere"""
    data = PowerInput(base=base, exp=exp)
    def worker():
        result = power(data.base, data.exp)
        click.echo(f"Rezultatul este: {result}")
        save_request("power", data.model_dump_json(), str(result))
    t = threading.Thread(target=worker)
    t.start()
    t.join()


@cli.command()
@click.option('--number', type=int, required=True)
def factorial_cmd(number):
    """Calculează factorialul unui număr"""
    data = FactorialInput(number=number)
    def worker():
        result = factorial(data.number)
        click.echo(f"Factorialul este: {result}")
        save_request("factorial", data.model_dump_json(), str(result))
    t = threading.Thread(target=worker)
    t.start()
    t.join()


@cli.command()
@click.option('--number', type=int, required=True)
def fib(number):
    """Calculează al n-lea număr din șirul Fibonacci"""
    data = FibonacciInput(number=number)
    def worker():
        result = fibonacci(data.number)
        click.echo(f"Numărul Fibonacci este: {result}")
        save_request("fibonacci", data.model_dump_json(), str(result))
    t = threading.Thread(target=worker)
    t.start()
    t.join()


if __name__ == '__main__':
    cli()
