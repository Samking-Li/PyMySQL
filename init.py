from sqlalchemy import create_engine

user = input("请输入账号：")
password = input("请输入密码：")

engine=create_engine('mysql+pymysql://'+user+':'+password+'@localhost/student_course')#数据库连接引擎
