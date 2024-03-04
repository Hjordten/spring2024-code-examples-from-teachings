def uppercase_decorator(func):
    def wrapper(*args):
        original_result = func(*args)
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"


