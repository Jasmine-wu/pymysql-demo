import os
import time
import math


def create_dir(file_paths):
    for path in file_paths:
        if not os.path.exists(path):
            os.mkdir(path)


# create_dir(["./Os", "./Time", "./urllib", "Math"])

def create_file():
    if not os.path.exists("./file.txt"):
        file = open("./file.txt", "w", encoding="utf-8")
        file.close()


def copy_file_to(to_file):
    file = open("./file.txt", "r")
    text = file.read()
    file.close()
    file = open(to_file, "w")
    file.write(text)
    file.close()


# copy_file_to("./copy_file.txt")

def get_time():
    # 时间戳可作为唯一标识符
    print(time.time())

    # 当前时间
    print(time.localtime())

    # 2天前的时间
    seconds = time.time() - 60 * 60 * 24 * 2
    print(time.localtime(seconds))
    print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(seconds)))

    print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))


# get_time()
def get_math():
    print(math.ceil(5.5))
    print(math.floor(5.5))
    print(math.sqrt(100))
# get_math()

# if __name__ == '__main__':

# print("time", time.localtime())
