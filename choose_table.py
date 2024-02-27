import table1
import table2
import table3
import table4
import table5


def choose_table_mode():
    while True:  # while循环使功能主界面能一直供用户使用，直到用户不需要为止
        print('学生成绩管理系统，请选择接下来要操作的表'.center(71,'-'))#功能选项也是在一个方框内
        print('{0:<3}{1:<72}\t{2:>}'.format('|','1.学生表;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','2.教师表;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','3.课程表;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','4.选课表;','|'))
        print('{0:<3}{1:<69}\t{2:>}'.format('|','5.教师授课表;','|'))
        print('{0:<3}{1:<72}\t{2:>}'.format('|','0.退出程序;','|'))
        print('-'*80,'\n')
        select = input("请输入你的选择>>")
        if select == '1':
            table1.table1_mode()# 函数调用或传参使用
        elif select == '2':
            table2.table2_mode()
        elif select == '3':
            table3.table3_mode()
        elif select == '4':
            table4.table4_mode()
        elif select == '5':
            table5.table5_mode()
        elif select == '0':
            print('-'*70)
            break
        else:
            print(">>你的输入错误！请按照提示重新输入！\n")  # 错误输入格式提醒
            continue

if __name__ == '__main__':
        choose_table_mode()
