
import logging
import threading
from time import sleep, ctime

"""
     _thread lock操作麻烦
    threading自带锁
"""

logging.getLogger().setLevel(logging.INFO)
secs = [2,4]

def loop(loop_name, nsec):

    logging.info("start loop" + str(loop_name) + " at "+ ctime())
    sleep(nsec)
    logging.info("end loop" + str(loop_name) + " at "+ ctime())

def main():

    logging.info("start all at {}".format(ctime()))
    loop_names = range(len(secs))

    threads = []

    for i in loop_names:
        thread = threading.Thread(target=loop, args=(i, secs[i]))
        threads.append(thread)

    for i in loop_names:
        # 启动线程
        threads[i].start()

    for i in loop_names:
        # 等待线程,会等上一个线程结束
        threads[i].join()

    logging.info("end all at {}".format(ctime()))


if __name__ == '__main__':
    main()