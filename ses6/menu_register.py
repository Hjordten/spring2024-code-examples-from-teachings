registered_functions = {}

def register(func):
    registered_functions[func] = func
    return func

@register
def home():
    return ("I'm the home page",)

@register
def about():
    return ("I'm the about page",)

# Accessing registered functions
print(registered_functions)

# Accessing a specific function
home_page_function = registered_functions.get(home)
if home_page_function:
    print(home_page_function()[0])  # Accessing the first element of the tuple
