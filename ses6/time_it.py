import time
import datetime

# Define the decorator function
def time_it_decorator(func):
    # Define the wrapper function inside the decorator
    def wrapper(*args):
        # Record the start time before executing the function
        start_time = time.time()
        
        # Execute the original function and store its result
        result = func(*args)
        
        # Record the end time after the function execution
        end_time = time.time()
        
        # Calculate the execution time
        execution_time = end_time - start_time
        
        # Open the log file in append mode and write the timestamp and execution time
        # Note: Removed func.__name__ to avoid using the function's name
        with open('logfile.txt', 'a') as f:
            f.write(f'{datetime.datetime.now()} - Function took {execution_time:.4f} seconds to execute.\n')
        
        # Return the result of the original function
        return result
    # Return the wrapper function from the decorator
    return wrapper

# Apply the decorator to the add function
@time_it_decorator
def add(*args):
    # Sum the arguments and return the result
    return sum(args)
