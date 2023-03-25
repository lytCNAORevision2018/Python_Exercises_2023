'''
4.编写程序，输入正整数n，打印由*组成且高为n的等腰三角形。
【注意】运行效果应如下所示，格式错误算结果错误。
测试1：（第1行为输入，其余行为输出）
5
    *
   ***
  *****
 *******
*********

'''
n = int(input())
for i in range(1,(n+1)):
    num1 = n-i
    for j in range(num1):
        print(' ' ,end ='')
    num2 = 2*i-1
    for j in range(num2):
        print("*",end ='')
    print()
