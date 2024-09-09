# import logging
# def log_execution_time(func):
#     logging.basicConfig(filename = "assignment5.log", level=logging.DEBUG,
#                         format='%(asctime)s -%(levelname)s -%(message)s')
#     def wrapper(*args, **kwargs):
#         # logging.basicConfig(level=logging.DEBUG,
#         #                    format='%(asctime)s -%(levelname)s -%(message)s)')
#         logging.debug(func.__name__ + " has begun")
#         result = func(*args, **kwargs)
#         logging.debug(func.__name__ + " has finished")
#         return result
#     return wrapper
#

## assignment 5 using advanced configuration
import logging
def log_execution_time(func):
    asnmt = logging.getLogger('logging using advanced logging')
    handler = logging.FileHandler('advanced_asnmt.log')
    formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    asnmt.addHandler(handler)
    asnmt.setLevel(logging.INFO)

    def wrapper(*args, **kwargs):
        # logging.basicConfig(level=logging.DEBUG,
        #                    format='%(asctime)s -%(levelname)s -%(message)s)')
        asnmt.info (func.__name__ + " has begun")
        result = func(*args, **kwargs)
        asnmt.debug (func.__name__ + " has finished")
        return result
    return wrapper




@log_execution_time
def greet(name):
    print(f"Hello, {name}")

greet("Alice")