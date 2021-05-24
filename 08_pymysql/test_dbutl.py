from dbutl import DBUtil
sql = "select * from t_book;"
result = DBUtil.exe_sql(sql)
print(result)

sql = "select * from t_book;"
