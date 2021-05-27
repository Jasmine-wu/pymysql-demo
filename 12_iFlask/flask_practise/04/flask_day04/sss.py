

import requests
import time



from threading import Thread

def task():
    res=requests.get('http://127.0.0.1:5000')
    print(res)

if __name__ == '__main__':
    ctimt=time.time()
    ll=[]
    for i in range(5000):
        t=Thread(target=task)
        t.start()
        ll.append(t)
    for t in ll:
        t.join()
    print(time.time()-ctimt)  #1.9011645317077637   #2.0673177242279053

    # 没有数据库连接池19.57759714126587
    #有数据库连接池：19.263076305389404