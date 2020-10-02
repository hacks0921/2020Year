#예제 1번
import threading

def execute(number):
    """
    쓰레드에 실행할 함수
    """
    print(threading.current_thread().getName(),number)

if __name__=='__main__':
    for i in range(1,8): # 1~7 실행
        my_thread = threading.Thread(target=execute, args=(i,))
        my_thread.start()
