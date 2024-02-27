from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from init import engine

db=declarative_base()#这个是sqlalchemy内部封装的一个方法，通过其构造一个基类，这个基类和它的子类，可以将Python类和数据库表关联映射起来

class STU(db):#在所选定的数据库，利用这个类模型建立数据表，并定义其中的类属性对应表中的字段属性
    __tablename__='student'#命名

    sname=Column(String(45))
    ssex=Column(String(45))
    sage=Column(Integer)
    sid=Column(String(45),primary_key=True)
    sdept=Column(String(45))

db.metadata.create_all(engine)#创建数据表，原本存在即忽略
DbSession = sessionmaker(bind=engine)
session = DbSession()#session用于创建程序和数据库之间的会话

def stu_information_single():  # 输入
    sname = input("请输入学生姓名：")
    ssex = input("请输入该学生的性别：")
    sage = input("请输入该学生的年龄：")
    sid = input("请输入该学生的学号：")
    sdept = input("请输入该学生的系：")
    user = STU(sname=sname, ssex=ssex, sage=sage, sid=sid, sdept=sdept)
    session.add(user)
    session.commit()
    print('>>添加成功！\n')

def stu_change():  # 修改
    sid = input("请输入该学生的学号：")
    print('{0:<3}{1:<72}\t{2:>}'.format('|','1.姓名;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','2.性别;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','3.年龄;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','4.学号;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','5.系;','|'))
    print('{0:<3}{1:<72}\t{2:>}'.format('|','0.所有;','|'))
    print('-'*80,'\n')
    select = input("您想修改的项目是>>")
    if select == '0':
        users = session.query(STU).filter_by(sid=sid).first()#先查找出对应学号的对象，在重新添加信息覆盖之前的信息，达到修改的目的
        users.cname = input("请输入该学生的姓名：")
        users.ssex = input("请输入该学生的性别：")
        users.sage = input("请输入该学生的年龄：")
        users.sid = input("请输入该学生的学号：")
        users.sdept = input("请输入该学生的系：")
        session.add(users)
        session.commit()
    elif select =='1':
        users = session.query(STU).filter_by(sid=sid).first()
        users.sname = input("请输入该学生的姓名：")
        session.add(users)
        session.commit()
    elif select =='2':
        users = session.query(STU).filter_by(sid=sid).first()
        users.ssex = input("请输入该学生的性别：")
        session.add(users)
        session.commit()
    elif select =='3':
        users = session.query(STU).filter_by(sid=sid).first()
        users.sage = input("请输入该学生的年龄：")
        session.add(users)
        session.commit()
    elif select =='4':
        users = session.query(STU).filter_by(sid=sid).first()
        users.sid = input("请输入该学生的学号：")
        session.add(users)
        session.commit()
    elif select =='5':
        users = session.query(STU).filter_by(sid=sid).first()
        users.sdept = input("请输入该学生的系：")
        session.add(users)
        session.commit()
    return

def stu_delete():  # 删除学生信息
    sid = str(input("请输入要删除学生信息的学号："))
    result=session.query(STU).filter_by(sid=sid).first()
    if result != None:#若返回对象不为为空，继续删除操作
        session.delete(result)
        session.commit()
        print('>>删除成功')
    else:
        print('>>查无此人或你的输入有误！')

def stu_check():  # 查找学生信息
    sid = str(input("请输入要查询学生信息的学号："))
    result=session.query(STU).filter_by(sid=sid).first()
    if result != None:
        print('-' * 56)
        print('|{0:^22}|{1:^6}|{2:^6}|{3:^5}|{4:^5}|'.format('姓名', '性别', '年龄', '学号', '系'))
        print('-' * 56)
        print('|{0:^22}\t|{1:^6}\t|{2:^6}\t|{3:^5}\t|{4:^5}|'.format(result.sname, result.ssex, result.sage, result.sid, result.sdept))
        print('-' * 56)
    else:
        print('>>查无此人或你的输入有误！')

def stu_all(*b):  # 显示该系统中的所有学生信息数据
    all_result=session.query(STU).all()
    print('<全部学生信息表>' .center(52,'—'))
    print('|{0:^22}|{1:^6}|{2:^6}|{3:^5}|{4:^5}|'.format('姓名', '性别', '年龄', '学号', '系'))#为了输出效果上构成一个表，输出格式进行了对应的调整
    print('-' * 56)#该表的横线分隔部分是由‘-’构成，如果想用其他符号也可（+=）
    for i in all_result:
        print('|{0:^20}\t|{1:^6}\t|{2:^6}\t|{3:^6}\t|{4:^6}|'.format(i.sname, i.ssex, i.sage, i.sid, i.sdept))
        print('-' * 56)
    print(">>已显示系统内所有人的信息！\n")

def table1_mode():
    while True:  # while循环使功能主界面能一直供用户使用，直到用户不需要为止

        print('教学信息管理系统，请选择系统功能'.center(71,'-'))#功能选项也是在一个方框内
        print('{0:<3}{1:<72}\t{2:>}'.format('|','1.输入学生信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','2.修改学生的相关信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','3.删除学生的相关信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','4.查询学生信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','5.显示所有学生的信息;','|'))
        print('{0:<3}{1:<72}\t{2:>}'.format('|','0.退出程序;','|'))
        print('-'*80,'\n')
        select = input("请输入你的功能选择>>")
        if select == '1':
            stu_information_single()  # 函数调用或传参使用
        elif select == '2':
            stu_change()    #同上
        elif select == '3':
            stu_delete()
        elif select == '4':
            stu_check()
        elif select == '5':
            stu_all()
        elif select == '0':
            print('-'*70)
            break
        else:
            print(">>你的输入错误！请按照提示重新输入！\n")  # 错误输入格式提醒
            continue

if __name__ == '__main__':
    table1_mode()
