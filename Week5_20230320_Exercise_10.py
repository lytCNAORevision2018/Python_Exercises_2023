'''
10.编写程序，实现n（n>=2)个分数相加。需要化简。
【注意】运行效果应如下，格式不同算错：
测试1：（第1、2、3行为输入，其中第一行输入的是分数的个数，第4行为输出）
2
1/3
2/3
1
测试2：（第1、2、3、4行为输入，其中第一行输入的是分数的个数，第5行为输出）
3
1/3
1/4
1/5
47/60
测试3：（第1、2、3、4、5行为输入，其中第一行输入的是分数的个数，第6行为输出）
4
1/2
5/6
4/5
3/4
2+53/60
'''
def zzxc(m:int,n:int)->int :
    max_v = max(m, n)
    min_v = min(m, n)
    r = max_v % min_v
    while r != 0:
        max_v = min_v
        min_v = r
        r = max_v % min_v
    return min_v


def fenshu(m: int, n: int) -> int:
    m_fz, m_fm = map(int, m.split('/'))
    n_fz, n_fm = map(int, n.split('/'))
    max_gb = zzxc(m_fm, n_fm)
    min_gy = m_fm * n_fm // max_gb
    m_xs = min_gy // m_fm
    n_xs = min_gy // n_fm
    new_fz = m_fz * m_xs + n_fz * n_xs
    yf_xs = zzxc(new_fz, min_gy)
    new_fz //= yf_xs
    min_gy //= yf_xs
    return str(new_fz) + '/' + str(min_gy)


n = int(input())
ls = []
for i in range(0, n):
    ls.append(input())
for i in range(0, n - 1):
    ls[0] = fenshu(ls[0], ls[1])
    del ls[1]
fz, fm = map(int, ls[0].split('/'))
temp1 ,temp2 = divmod(fz,fm)
if temp2 == 0:
    print(temp1)
else:
    print(str(temp1)+'+'+str(temp2)+'/'+str(fm))

