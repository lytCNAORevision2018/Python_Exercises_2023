'''
6.编写程序，输入正整数n（n为奇数），打印由*组成且高为n的空心菱形。
【注意】运行效果应如下所示，格式错误算结果错误。
测试1：（第1行为输入，其余行为输出）
7
   *
  * *
 *   *
*     *
 *   *
  * *
   *
'''
layer = int(input())
for i in range(1,layer//2+2):
	num1 = layer//2+1-i
	for j in range(num1):
		print(" ",end="")
	num2 = i*2-1
	for j in range(num2):
		if j==0 or j == num2-1:        #判断是否打印第一个或最后一个星号
			print("*",end= "")
		else:
			print(" ",end = "")
	print("")
for i in range(layer//2,0,-1):
	num1 = layer//2+1-i
	for j in range(num1):
		print(" ",end="")
	num2 = i*2-1
	for j in range(num2):
		if j==0 or j == num2-1:
			print("*",end="")
		else:
			print(" ",end = "")
	print("")
