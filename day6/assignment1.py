def dec_with_arg(a,b):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(a +" "+ func.__name__)
            result = func(*args,**kwargs)
            print(b+" " + func.__name__)
            return result
        return wrapper
    return decorator

@dec_with_arg('start','finished')
def greet(name):
    print("Hello " + name)


greet('John')