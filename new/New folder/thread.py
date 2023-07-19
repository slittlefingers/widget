# import threading

# def task():
#     print("Task is running...")

# # 创建线程
# thread = threading.Thread(target=task)

# # 启动线程
# thread.start()

# import threading

# lock = threading.Lock()

# def task():
#     with lock:
#         print("Task is running...")

# thread1 = threading.Thread(target=task)
# thread2 = threading.Thread(target=task)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()


# import threading
# import time

# def task():
#     time.sleep(5)
#     print("Task is completed!")

# thread = threading.Thread(target=task)
# thread.start()

# # Main thread will wait until `thread` is done
# thread.join()

# print("All done!")

# from multiprocessing import Process

# def task():
#     print("Task is running...")

# # 创建进程
# process = Process(target=task)

# # 启动进程
# process.start()

# from multiprocessing import Process, Queue

# def worker(q):
#     q.put('Hello from worker process')

# def main():
#     q = Queue()
#     p = Process(target=worker, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# if __name__ == '__main__':
#     main()



# from multiprocessing import Process, Lock

# def printer(item, lock):
#     """
#     输出一个项目到标准输出
#     """
#     lock.acquire()
#     try:
#         print(item)
#     finally:
#         lock.release()

# if __name__ == '__main__':
#     lock = Lock()
#     items = ['tango', 'foxtrot', 10]
#     for item in items:
#         p = Process(target=printer, args=(item, lock))
#         p.start()


import time
# in this function
def my_progress_bar(how_long):
    bar_long=20
    # in the print bar we can see that how long is now this staff is (progress)
    filled_length=int(how_long*bar_long)
    # \033[ ] change the color first part is to out the filled part, then we use total long decrease the filled part to get the rest part
    bar='\033[32m-\033[0m' * filled_length  + '-' * (bar_long-filled_length)
    # return one dicimal and
    return f'|{bar}| {how_long*100:.1f}%'

def print_bar(rang_number):
    for i in range(rang_number):
        progress = i / 10
        progress_bar = my_progress_bar(progress)
        # in end='/r' this way the point will not change the direction
        print(progress_bar, end='\r')
        time.sleep(1)
print_bar(11)