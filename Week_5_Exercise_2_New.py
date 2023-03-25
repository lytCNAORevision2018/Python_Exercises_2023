def isprime(n):#定义判断素数的函数
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
tri_list = []#初始化三位数列表
four_list = []#初始化四位数列表
five_list = []#初始化五位数列表
for triple_a in range(1, 10):
    for triple_b in range(0, 10):
        for triple_c in range(0, 10):
            if isprime(100 * triple_a + 10 * triple_b + triple_c) and isprime(10 * triple_a + triple_b) and isprime(triple_a):
                tri_list.append(100 * triple_a + 10 * triple_b + triple_c)#add numbers to tri
for four_a in range(1,10):
    for four_b in range(0,10):
        for four_c in range(0,10):
            for four_d in range(0,10):
                if isprime(1000*four_a+100*four_b+10*four_c+four_d) and isprime(100*four_a+10*four_b+four_c) and isprime(10*four_a+four_b) and isprime(four_a):
                    four_list.append(1000*four_a+100*four_b+10*four_c+four_d)#add numbers to four
for five_a in range(1,10):
    for five_b in range(1,10):
        for five_c in range(1,10):
            for five_d in range(1,10):
                for five_e in range(1,10):
                    if isprime(10000 * five_a + 1000 * five_b + 100 * five_c +10 * five_d+five_d) and isprime(
                        1000 * five_a + 10 * five_b + five_c) and isprime(10 * five_a + five_b) and isprime(five_a):
                        five_list.append(10000*five_a+1000*five_b+100*five_c+10*five_d+five_e)
final_list = tri_list+four_list+five_list
n = int(input())
if n in final_list:
    print("Yes")
else:
    print("No")