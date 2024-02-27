from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from init import engine

db=declarative_base()#这个是sqlalchemy内部封装的一个方法，通过其构造一个基类，这个基类和它的子类，可以将Python类和数据库表关联映射起来

class COU(db):#在所选定的数据库，利用这个类模型建立数据表，并定义其中的类属性对应表中的字段属性
    __tablename__='course'#将该表命名为stu

    cname=Column(String(45))
    cid=Column(String(45), primary_key=True)#由于学号是唯一的，并且我们以学号作为搜索的参考，所以用unique设为True，不能重复该值

db.metadata.create_all(engine)#创建数据表，原本存在即忽略
DbSession = sessionmaker(bind=engine)
session = DbSession()#session用于创建程序和数据库之间的会话，所有对象的载入和保存都需要通过session对象roo

def stu_information_single():  # 输入
    cname = input("请输入课程名：")
    cid = input("请输入该课程编号：")
    user = COU(cname=cname, cid=cid)#左边的name是数据库(模型类)对应的列名name，右边name是我们input收集的变量
    session.add(user)
    session.commit()
    print('>>添加成功！\n')

def stu_change():  # 修改
    cid = str(input("请输入该学生的学号："))
    print('{0:<3}{1:<72}\t{2:>}'.format('|','1.课程名;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','2.课程编号;','|'))
    print('{0:<3}{1:<72}\t{2:>}'.format('|','0.所有;','|'))
    print('-'*80,'\n')
    select = input("您想修改的项目是>>")
    if select == '0':
        users = session.query(COU).filter_by(cid=cid).first()#先查找出对应学号的对象，在重新添加信息覆盖之前的信息，达到修改的目的
        users.cname = input("请输入课程名：")
        users.cid = input("请输入课程编号：")
        session.add(users)
        session.commit()
    elif select =='1':
        users = session.query(COU).filter_by(cid=cid).first()
        users.cname = input("请输入课程名：")
        session.add(users)
        session.commit()
    elif select =='2':
        users = session.query(COU).filter_by(cid=cid).first()
        users.cid = input("请输入课程编号：")
        session.add(users)
        session.commit()
    return

def stu_delete():  # 删除学生信息
    cid = str(input("请输入要删除课程信息的课程编号："))
    result=session.query(COU).filter_by(cid=cid).first()
    if result != None:#若返回对象不为为空，继续删除操作
        session.delete(result)
        session.commit()
        print('>>删除成功')
    else:
        print('>>查无此人或你的输入有误！')

def stu_check():  # 查找学生信息
    cid = input("请输入要查询的课程编号：")
    result=session.query(COU).filter_by(cid=cid).first()
    if result != None:
        print('-' * 56)
        print('|{0:^22}|{1:^6}|'.format('课程名','课程编号'))
        print('-' * 56)
        print('|{0:^22}\t|{1:^6}|'.format(result.cname,result.cid,))
        print('-' * 56)
    else:
        print('>>查无此课或你的输入有误！')

def stu_all(*b):  # 显示该系统中的所有学生信息数据
    all_result=session.query(COU).all()
    print('<全部课程信息表>' .center(52,'—'))
    print('|{0:^22}|{1:^6}|'.format('课程名', '课程编号'))#为了输出效果上构成一个表，输出格式进行了对应的调整
    print('-' * 56)#该表的横线分隔部分是由‘-’构成，如果想用其他符号也可（+=）
    for i in all_result:
        print('|{0:^20}\t|{1:^6}|'.format(i.cname,  i.cid))
        print('-' * 56)
    print(">>已显示系统内所有课程的信息！\n")

def table3_mode():
    while True:  # while循环使功能主界面能一直供用户使用，直到用户不需要为止

        print('课程管理系统，请选择系统功能'.center(71,'-'))#功能选项也是在一个方框内
        print('{0:<3}{1:<72}\t{2:>}'.format('|','1.输入课程信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','2.修改课程的相关信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','3.删除课程的相关信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','4.查询课程信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','5.显示所有课程的信息;','|'))
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
    table3_mode()
