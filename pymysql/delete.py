import pymysql
cont = pymysql.connect(host="localhost", port=3306, user="root", password="12345678", database="Books",autocommit=True)
# cont.cursor()
cursor = cont.cursor()
# 2).删除图书(title:东游记)
sql = "delete from t_book where title='东游记';"

cursor.execute(sql)
cursor.close()
cont.close()