'''
9.编写程序，输入两个分数，计算并输出求和的结果(需化简）。
【注意】运行效果应如下，格式不同算错：
测试1：（第1、2行为输入，第3行为输出）
1/5
4/5
1
测试2：（第1、2行为输入，第3行为输出）
1/15
1/10
1/6
测试3：（第1、2行为输入，第3行为输出）
7/3
3/4
3+1/12
'''
def zzxc(m, n):
    max_v = max(m, n)
    min_v = min(m, n)
    r = max_v % min_v
    while r != 0:
        max_v = min_v
        min_v = r
        r = max_v % min_v
    return min_v


def fenshu(m, n):
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


n = 2
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




    '''
    if fz % fm == 0:
    print(fz // fm)
elif type(fz//fm) == int:
    print(str(fz//fm) +'/'+str((fz-fm)//fm))
else:
    print(str(fz) + '/' + str(fm))
    '''


