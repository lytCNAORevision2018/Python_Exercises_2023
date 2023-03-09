'''
6.编写程序，对于给定的一个百分制成绩，输出相应的五分制成绩。
设90分以及以上为A
80-89分为B
70-79分为C
60-69分为D
60分以下为E
测试1：（第1行为输入，第2行为输出）
96
A
测试2：（第1行为输入，第2行为输出）
70  
C
测试3：（第1行为输入，第2行为输出）
55 
E

'''
x = int(input())
if x > 100 or x<0:
    pass
elif x >= 90:
    rklevel = 'A'
elif 80<= x :
    rklevel = 'B'
elif 70 <= x :
    rklevel = 'C'
elif 60 <= x:
    rklevel = 'D'
else:
    rklevel = 'E'
print(rklevel)
