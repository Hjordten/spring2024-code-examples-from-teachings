import datetime

def decorator(func):
    def wrapper(*args):
        f = open('logfile.txt', 'a')
        f.write(f'{datetime.datetime.now()} \n')        
        return func(*args)
    return wrapper
    
#@decorator
def add(*args):
    return sum(args)


add = decorator(add)


