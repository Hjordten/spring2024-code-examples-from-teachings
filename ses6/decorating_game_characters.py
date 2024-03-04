# ability_decorator.py

def ability_decorator(skill):
    def decorator(func):
        def wrapper(*args):
            original_result = func(*args)
            modified_result = f"{original_result}, the {skill} character"
            return modified_result
        return wrapper
    return decorator

@ability_decorator("sharpshooter")
@ability_decorator("stealthy")
def player():
    return "I'm the player character"

# Apply multiple decorators to the player function
@ability_decorator("hacker")
@ability_decorator("invisible")
def player_with_multiple_abilities():
    return "I'm the player character"
