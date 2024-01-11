import threading, os
from time import sleep

os.system('cls')

def run():
    while True:
        sleep(0.5)
        print('running')
        print(thread_run)
        if not thread_run['camera1']:
            print('killing process')
            return

thread_run = { 'camera1': True }
t1 = threading.Thread(target=run)
t1.start()
sleep(2)
thread_run['camera1'] = False

t1.join()