# menu_register.py

menu_register = []

def register(func):
    """
    A decorator to register functions in the menu_register list.
    """
    # Add the function to the register
    menu_register.append(func)
    return func

@register
def home():
    return ("I'm the home page")

@register
def about():
    return ("I'm the about page")
