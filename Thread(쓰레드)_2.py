import logging
import threading

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = logging.StreamHandler()
    fmt = '[%(asctime)s] = %(threadName)s ----- %(levelname)s   >>>   %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def execute(number, logger):
    logger.debug('excute function excuting Test')
    result = number *2
    logger.debug('excute funciton end with: {}'.format(result))

if __name__ =='__main__':
    logger = get_logger()
    for i, name in enumerate(['kim','lee','park','cho','hong']):
        my_thread = threading.Thread(
            target=execute, name=name, args=(i,logger))
            # 실행할 함수,  스레드의 이름 안써도 무방 , args : target에 넘겨질 인자로 튜플형식으로 전달(vaule,0)
        my_thread.start()