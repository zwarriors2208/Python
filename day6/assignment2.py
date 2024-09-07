import time

def log_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        a = time.time()
        print('starting' + func.__name__)
        result = func(*args, **kwargs)
        b = time.time()
        print(f"time required for function {func.__name__} to execute is: {b-a}")
        return result
    return wrapper

@log_execution_time
def greet(name):
    print(f"Hello {name}")
    time.sleep(2)


# greet('ankkit')
