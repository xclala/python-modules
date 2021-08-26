
def add_fib_all(n:int) -> int:
    """python_version>=3.6"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
        