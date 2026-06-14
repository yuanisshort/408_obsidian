# -*- coding:cp936 -*-
'''------------------------------------------------------
【程序改错】
---------------------------------------------------------

题目：编写input_stu ()和output_stu ()函数输入，输出5个学
      生的数据记录。
      请改正程序中的错误，使它能得出正确的结果。

---------------------------------------------------------
注意：不可以增加或删除程序行，也不可以更改程序的结构。
------------------------------------------------------'''
N = 5
student = []
for i in range(5):
    student.append(['','',[]])
 
def input_stu(stu):
    for i in range(N):
        stu[i][0] = input("请输入学生学号: ")
        stu[i][1] = input("请输入学生姓名: ")
        for j in range(3):            
            #**********FOUND**********
            stu[i][2].append(int(input("请输入第%d个成绩,: " %(j + 1))))
 
def output_stu(stu):    
    #**********FOUND**********
    for i in range(N):
        print('%-6s%-10s' % ( stu[i][0],stu[i][1] ))
        for j in range(3):            
            #**********FOUND**********
            print('%-8d'%stu[i][2][j])

def main():    
    input_stu(student)
    output_stu(student) 
   
if __name__ == '__main__':
    main()
