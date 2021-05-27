
from flask import Flask
from flask_script import Manager
app = Flask(__name__)
manager=Manager(app)


# 自定制命令 Python manage.py createsuperuser
@manager.command
def custom(arg):
    """
    自定义命令
    python manage.py custom 123
    :param arg:
    :return:
    """
    print(arg)


@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def cmd(name, url):
    """
    自定义命令（-n也可以写成--name）
    执行： python manage.py  cmd -n lqz -u http://www.oldboyedu.com
    执行： python manage.py  cmd --name lqz --url http://www.oldboyedu.com
    :param name:
    :param url:
    :return:
    """
    print(name, url)


if __name__ == '__main__':
    manager.run()


