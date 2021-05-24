import pytest
import os
import shlex
import signal
import subprocess
import yaml
# 为什么不能设置成function和menthod级别？会报keyboardInterrupt的异常，也就是pytest会截获control+c命令，导致程序中断
# 如果一个menthod里面参数化多条测试用例，当执行第一条时，Control+c被截获导致程序退出。
# 如何解决？换中断命令，不要用control+c
# 自动应用到每个module
# @pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(scope="module", autouse=True)
def record():
    # subprocess python一个子程序，可以执行命令
    # shell 脚本模式：所有命令可以写在一行调用，但由于这个脚本会运行在多个操作系统上，window-cmd, linux-bash
    # stdout=subprocess.Popen 正确输出
    # stderr = subprocess.STDOUT 错误输出
    # 对命令进行解析，解析成非shell风格
    cmd = shlex.split("scrcpy --record temp.mp4")

    # 开启一个子线程运行命令
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.Popen, stderr=subprocess.STDOUT)

    # 打印输出
    print(p)

    # 等10秒 不要写死,用yield
    # sleep(10)
    yield

    # 中断录屏, 中断命令不要用CTRL_C_EVENT mac :kill pid window:task kill
    os.kill(p.pid, signal.CTRL_C_EVENT)

    # 待测试
    # os.kill(p.pid, signal.SIGKILL)

