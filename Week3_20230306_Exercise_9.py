'''
9.编写程序，输入年、月、日，计算该月还剩余多少天。
【注意】运行效果应如下所示，格式错误算结果错误。
要求使用if-elif语句实现。
测试1：（第1行为输入，第2行为输出）
2022 11 26
4
测试2：（第1行为输入，第2行为输出）
2020 2 15
14

'''
year,month,day = map(int,input().split(' ',2))
if year %4 == 0 and year% 400 !=0 or year% 400 ==0:#Runnian!
    if month ==1:
        day_of_the_month= 31
    elif month == 2:
        day_of_the_month = 29
    elif month ==3:
        day_of_the_month= 31
    elif month ==4:
        day_of_the_month= 30
    elif month ==5:
        day_of_the_month= 31
    elif month ==6:
        day_of_the_month= 30
    elif month ==7:
        day_of_the_month= 31
    elif month ==8:
        day_of_the_month= 31
    elif month ==9:
        day_of_the_month= 30
    elif month ==10:
        day_of_the_month= 31
    elif month ==11:
        day_of_the_month= 30
    elif month ==12:
        day_of_the_month= 31
else:
    if month ==1:
        day_of_the_month= 31
    elif month == 2:
        day_of_the_month = 28
    elif month ==3:
        day_of_the_month= 31
    elif month ==4:
        day_of_the_month= 30
    elif month ==5:
        day_of_the_month= 31
    elif month ==6:
        day_of_the_month= 30
    elif month ==7:
        day_of_the_month= 31
    elif month ==8:
        day_of_the_month= 31
    elif month ==9:
        day_of_the_month= 30
    elif month ==10:
        day_of_the_month= 31
    elif month ==11:
        day_of_the_month= 30
    elif month ==12:
        day_of_the_month= 30
days_left_in_the_month = day_of_the_month - day 
print(days_left_in_the_month)
