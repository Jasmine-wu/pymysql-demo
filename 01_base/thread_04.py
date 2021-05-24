"""
    继承thread类，重写run
"""

import logging
import threading
from time import sleep, ctime

logging.getLogger().setLevel(logging.INFO)
secs = [2,4]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


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
        thread = MyThread(loop, (i, secs[i]), loop.__name__)
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