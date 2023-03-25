'''
2.一个素数，若依次从低位去掉一位、两位、······若所得各数仍都为素数，则称该数为超级素数。例如：由于239、23、2均为素数，则239为超级素数。
编写程序，输入正整数n，判断是否为超级素数。如果是，输出"Yes"，如果不是，输出"No"。
【注意】运行效果应如下所示，格式错误算结果错误。
测试1：（第1行为输入，第2行为输出）
239
Yes
测试1：（第1行为输入，第2行为输出）
249
No
'''
def SuperPrime(x:int)->bool:
    for i in range(2,x):
        if x%i == 0:
            k = len(str(x))
            j = -1
            for m in range(len(str(x))):
                list = []
                list.append(SuperPrime(str(x)[::j-1]))
                j-=1
                if list.count(True) == len(str(x)):
                    return True
        else:
            return True
h = int(input())
if SuperPrime(h) == False:
    print("No")
else:
    print("Yes")
