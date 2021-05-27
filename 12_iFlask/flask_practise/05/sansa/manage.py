#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
生成依赖文件：
    pipreqs ./

"""
from sansa import create_app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sansa import db
app = create_app()
# flask-script的操作
manager=Manager(app)
# flask_migrate的操作，  必须跟flask-script合用
Migrate(app,db)
# 相当于你写了一个db函数
# 就支持python manage.py db init
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # app.run()
    manager.run()
