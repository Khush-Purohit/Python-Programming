def fibo():
    a,b=0,1

    while True:
        yield b
        a,b=b,a+b


fib_series = fibo()
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))