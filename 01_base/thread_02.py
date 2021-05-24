
import logging
import _thread
from time import sleep, ctime

logging.getLogger().setLevel(logging.INFO)
secs = [2,4]

def loop(loop_name, nsec, lock):

    logging.info("start loop" + str(loop_name) + " at "+ ctime())
    sleep(nsec)
    logging.info("end loop" + str(loop_name) + " at "+ ctime())
    lock.release()

def main():

    logging.info("start all at {}".format(ctime()))
    loop_names = range(len(secs))
    locks = []

    for i in loop_names:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in loop_names:
        _thread.start_new_thread(loop, (i, secs[i], locks[i]))

    # 当子线程结束，主线程自动结束
    for i in loop_names:
        while locks[i].locked(): pass

    logging.info("end all at {}".format(ctime()))

"""
     _thread 开启的线程，当主线程跑完以后，会强行把所有子线程kill掉
     所有这里要加sleep(6)
     _thread 没有守护线程的概念
     强行等6秒，如果不知道各个线程会耗时多久怎么办？可否做到主动监听loop0 loop1，当他们退出了,我也推出？
     _thread提供了锁的概念可以做到
"""

if __name__ == '__main__':
    main()