# First class functions (objects)

def f1(p):
    return p



def foo():
    print('Hello from foo')



# Inner functions
def foo():
    
    # define
    def bar():
        return 'From bar'
    
    #execute
    return bar()

# Decorators

def addtekst(func):
    def wrapper(*args):
        print('Summen af de to tal: ')
        func(*args)
    return wrapper

@addtekst
def add(n1, n2):
    print(n1 + n2)


# add = addtekst(add)



