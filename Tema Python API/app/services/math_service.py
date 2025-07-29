def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Number must be non-negative.")
    return 1 if n == 0 else n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Number must be non-negative.")
    if n in [0, 1]:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def power(base: float, exp: float) -> float:
    return base ** exp
