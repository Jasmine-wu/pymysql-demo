# 目录的遍历

import os


def get_file(path, rule=''):
    files = []
    for fpath, dirs, fs in os.walk(path):
        # print("fpath is :", fpath)
        # print("dirs is :",dirs)
        # print("fs is :",fs)

        for f in fs:
            if os.path.join(fpath, f).endswith(rule):
                files.append(f)
    return files


if __name__ == '__main__':
    print(get_file("/Users/neil/Desktop/bro"))
