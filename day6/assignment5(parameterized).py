import logging


def log_exe_time_parameters(log_file):
    logging.basicConfig(filename=log_file, level=log_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def decorator(funct):
        def wrapper(*args, **kwargs):
            logging.log(log_level, f'Starting {funct.__name__}')
            result = funct(*args, **kwargs)
            logging.log(log_level, f'Finished {funct.__name__}')
            return result
        return wrapper
    return decorator

@log_exe_time_parameters
def loggggggg():
    logging.debug("log print debug message")
    logging.error("log print error message")
    logging.warning("log warning message")
    logging.critical("log critical message")
    logging.info("log info message")


loggggggg()
