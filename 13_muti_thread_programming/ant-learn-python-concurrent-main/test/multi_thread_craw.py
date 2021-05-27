import spider
import time
import threading

def print_time(func):
    def innner(*args, **kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        print("total time:   ", time.time() - start_time)
    return innner


@print_time
def single_craw():
    for url in spider.url:
        spider.craw(url)

@print_time
def multi_craw():

    threads=[]
    for url in spider.url:
        threads.append(threading.Thread(target=spider.craw, args=(url,)))

    for thread in threads:
        thread.start()

    # for thread in threads:
    #     thread.join()

if __name__=='__main__':
    single_craw()
    multi_craw()



