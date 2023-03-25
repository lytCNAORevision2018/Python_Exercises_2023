'''
3.编写程序，找出介于正整数A、B(A<B<10000)之间（包含A和B）的所有回文数，
并按从小到大输出这些回文数。输出时，每5个数一行，每个数占5位宽，左对齐。
【注意】运行效果应如下所示，格式错误算结果错误。
测试1：（第1行,为输入，其余行为输出）
1 100
1    2    3    4    5    
6    7    8    9    11   
22   33   44   55   66   
77   88   99

'''


def HuiWenShu(x:int) -> bool:
    return str(x)[::-1] == str(x)
A,B = map(int,input().split())
k = A
h = 0
list = []
for t in range(A, B+1):
    if HuiWenShu(t) == True:
        list.append(t)
for m in list:
    h += 1
    print(format(m, '<5'), end='')
    if h % 5 == 0:
        print()

    
