import logging
def log_to_file(log_file,log_level=logging.INFO):
    logging.basicConfig(filename=log_file,level=log_level,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def decorator(func):

        def wrapper(*args,**kwargs):
            logging.log(log_level,f'Calling {func.__name__}')
            result=func(*args,**kwargs)
            logging.log(log_level,f'Calling {func.__name__}')
            return result
        return wrapper
    return decorator
@log_to_file(log_file='custom_log.log',log_level=logging.DEBUG)
def greeting(name):
    print(f'Hello {name}')


greeting('Alice')
