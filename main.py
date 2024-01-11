import queue, threading, time, os

os.system('cls')

def basic_worker(queue2, thread_name):
    print(f"Starting {threading.currentThread().getName()} --- {thread_name} - thread_name \n")
    while True:
        ##do_work on item which might take 10-15 minutes to complete
        time.sleep(2) # to simulate work
        queue2.task_done()

def basic(queue2):
    for i in range(10):
        print('enqueuing', i)
        t = threading.Thread(target=basic_worker, args=(queue2, i))
        t.daemon = True
        t.start()
    queue2.join()       # block until all tasks are done
    print('got here' + '\n')

queue2 = queue.Queue()

for item in range(4):
    print(f'range {item} de 4')
    queue2.put(item)

basic(queue2)


print("End of program")
