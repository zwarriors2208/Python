import logging


logging.basicConfig(filename='basicConfig.log',level=logging.DEBUG, format='%(asctime)s -%(levelname)s -%(message)s)')

logging.debug('This is a debug message')
logging.info('Ths is an info message')
logging.warning('Ths is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#Advanced configuration
# logger=logging.getLogger('advancedConfig_logger')
# handler=logging.FileHandler('advancedConfig.log')
# formatter=logging.Formatter('%(asctime)s -%(levelname)s -%(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)
#
# logger.debug('Debug message')
# logger.info('Info message')