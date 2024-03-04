import time
import datetime

# 1. Define the decorator function
def time_it_decorator(func):
    # 2. Define the wrapper function inside the decorator
    def wrapper(*args):
        # 3. Record the start time before executing the function
        start_time = time.time()
        
        # 4. Execute the original function and store its result
        result = func(*args)
        
        # 5. Record the end time after the function execution
        end_time = time.time()
        
        # 6. Calculate the execution time
        execution_time = end_time - start_time
        
        # 7. Open the log file in append mode and write the timestamp and execution time
        with open('logfile.txt', 'a') as f:
            f.write(f'{datetime.datetime.now()} - Function {func.__name__} took {execution_time:.4f} seconds to execute.\n')
        
        # 8. Return the result of the original function
        return result
    # 9. Return the wrapper function from the decorator
    return wrapper

# 10. Apply the decorator to the add function
@time_it_decorator
def add(*args):
    # 11. Sum the arguments and return the result
    return sum(args)
