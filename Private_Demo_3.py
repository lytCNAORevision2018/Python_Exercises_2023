x = 10
while x>0:
    if x == 8:
        break
    if x%3!= 1:
        continue
    x -= 2
else:
    print('x=',x)
