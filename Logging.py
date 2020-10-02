import logging

logger = logging.getLogger(__name__)

streamHander = logging.StreamHandler()
fileHander = logging.FileHandler('./server.log')

logger.addHandler(streamHander)
logger.addHandler(fileHander)


# logging.basicConfig(filename='./server.log', level=logging.DEBUG)
logger.setLevel(level=logging.DEBUG)
logging.debug('1) my debug')
logging.info("2) info_test_Log")
logging.warning("3) seo_warning_Log")
logging.error('4) my error log')
logging.critical('5) my CRITICAL Log')