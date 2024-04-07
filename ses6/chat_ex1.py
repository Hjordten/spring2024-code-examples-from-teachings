import time

def time_decorator(func):
    def wrapper(*args):
        start = time.time
        x = func(*args)
        end = time.time - start
        print('time {end}')
        return x
    return wrapper

@time_decorator
def add(*args):
    return sum(args)
