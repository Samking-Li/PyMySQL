from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from init import engine

db=declarative_base()#这个是sqlalchemy内部封装的一个方法，通过其构造一个基类，这个基类和它的子类，可以将Python类和数据库表关联映射起来

class TABLE(db):#在所选定的数据库，利用这个类模型建立数据表，并定义其中的类属性对应表中的字段属性
    __tablename__='SC'#将该表命名为TC

    sid=Column(String(45), primary_key=True)
    cid=Column(String(45),primary_key=True)

db.metadata.create_all(engine)#创建数据表，原本存在即忽略
DbSession = sessionmaker(bind=engine)
session = DbSession()#session用于创建程序和数据库之间的会话，所有对象的载入和保存都需要通过session对象roo

def information():  # 输入
    sid = str(input("请输入学生学号："))
    cid = str(input("请输入学生选修课程："))
    user = TABLE(sid=sid, cid=cid)#左边的name是数据库(模型类)对应的列名name，右边name是我们input收集的变量
    session.add(user)
    session.commit()
    print('>>添加成功！\n')

def change():  # 修改
    sid = str(input("请输入该学生学号："))
    cid = str(input("请输入该学生选修的课号"))
    users = session.query(TABLE).filter_by(sid=sid, cid=cid).first()#先查找出对应学号的对象，在重新添加信息覆盖之前的信息，达到修改的目的
    print("您想将数据修改成：\n")
    users.sid = str(input("学号："))
    users.cid = str(input("选修的课号："))
    session.add(users)
    session.commit()
    return

def delete():  # 删除信息
    sid = str(input("请输入该学生学号："))
    cid = str(input("请输入选修的课号"))
    result=session.query(TABLE).filter_by(sid=sid, cid=cid).first()
    if result != None:#若返回对象不为为空，继续删除操作
        session.delete(result)
        session.commit()
        print('>>删除成功')
    else:
        print('>>查无此人或你的输入有误！')

def scheck():  # 查找授课信息
    sid = str(input("请输入要查询的学生学号："))
    result = session.query(TABLE).filter_by(sid=sid).all()
    if result != None:
        print('-' * 56)
        print('|{0:^22}|{1:^6}|'.format('学号', '课号'))
        print('-' * 56)
        for i in result:
            print('|{0:^22}\t|{1:^6}|'.format(i.sid, i.cid))
        print('-' * 56)
    else:
        print('>>查无此人或你的输入有误！')

def ccheck():  # 查找授课信息
    cid = str(input("请输入课号："))
    result=session.query(TABLE).filter_by(cid=cid).all()
    if result != None:
        print('-' * 56)
        for i in result:
            print('|{0:^22}\t|{1:^6}|'.format(i.sid, i.cid))
        print('-' * 56)
        print('|{0:^22}\t|{1:^6}|'.format(result.sid, result.cid))
        print('-' * 56)
    else:
        print('>>查无此课或你的输入有误！')


def all(*b):  # 显示该系统中的所有数据
    all_result=session.query(TABLE).all()
    print('<全部选课信息表>' .center(52,'—'))
    print('|{0:^22}|{1:^6}|'.format('学号', '课程号'))#为了输出效果上构成一个表，输出格式进行了对应的调整
    print('-' * 56)#该表的横线分隔部分是由‘-’构成，如果想用其他符号也可（+=）
    for i in all_result:
        print('|{0:^20}\t|{1:^6}|'.format(i.sid, i.cid))
        print('-' * 56)
    print(">>已显示系统内所有人的信息！\n")

def table4_mode():
    while True:  # while循环使功能主界面能一直供用户使用，直到用户不需要为止

        print('学生选课管理系统，请选择系统功能'.center(71,'-'))#功能选项也是在一个方框内
        print('{0:<3}{1:<72}\t{2:>}'.format('|','1.输入选课信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','2.修改选课信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','3.删除选课信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','4.通过学号查询选课信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','5.通过课程号查询选课信息;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','6.显示所有选课的信息;','|'))
        print('{0:<3}{1:<72}\t{2:>}'.format('|','0.退出程序;','|'))
        print('-'*80,'\n')
        select = input("请输入你的功能选择>>")
        if select == '1':
            information()  # 函数调用或传参使用
        elif select == '2':
            change()    #同上
        elif select == '3':
            delete()
        elif select == '4':
            scheck()
        elif select == '5':
            ccheck()
        elif select == '6':
            all()
        elif select == '0':
            print('-'*70)
            break
        else:
            print(">>你的输入错误！请按照提示重新输入！\n")  # 错误输入格式提醒
            continue

if __name__ == '__main__':
    table4_mode()
