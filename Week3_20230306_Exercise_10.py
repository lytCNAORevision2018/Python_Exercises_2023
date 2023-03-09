'''
10.编写程序，输入年、月、日，计算该年还剩余多少天。
要求使用if-elif语句实现。
【注意】运行效果应如下所示，格式错误算结果错误。
测试1：（第1行为输入，第2行为输出）
2020 1 31
335
测试2：（第1行为输入，第2行为输出）
2023 12 1
30

'''
year,month,day = map(int,input().split(' ',2))
if year %4 == 0 and year% 400 !=0 or year% 400 ==0:#Runnian!
#Vibration 'distance' is the days between the first day of the month to January 1st of the same year.
    days_of_the_whole_year = 366
    if month ==1:
        distance= 0
    elif month == 2:
        distance= 31
    elif month ==3:
        distance= 31+29
    elif month ==4:
        distance= 31+29+31
    elif month ==5:
        distance= 31+29+31+30
    elif month ==6:
        distance= 31+29+31+30+31
    elif month ==7:
        distance= 31+29+31+30+31+30
    elif month ==8:
        distance= 31+29+31+30+31+30+31
    elif month ==9:
        distance= 31+29+31+30+31+30+31+31
    elif month ==10:
        distance= 31+29+31+30+31+30+31+31+30
    elif month ==11:
        distance= 31+29+31+30+31+30+31+31+30+31
    elif month ==12:
        distance= 31+29+31+30+31+30+31+31+30+31+30
else:
    days_of_the_whole_year = 365
    if month ==1:
        distance= 0
    elif month == 2:
        distance= 31
    elif month ==3:
        distance= 31+28
    elif month ==4:
        distance= 31+28+31
    elif month ==5:
        distance= 31+28+31+30
    elif month ==6:
        distance= 31+28+31+30+31
    elif month ==7:
        distance= 31+28+31+30+31+30
    elif month ==8:
        distance= 31+28+31+30+31+30+31
    elif month ==9:
        distance= 31+28+31+30+31+30+31+31
    elif month ==10:
        distance= 31+28+31+30+31+30+31+31+30
    elif month ==11:
        distance= 31+28+31+30+31+30+31+31+30+31
    elif month ==12:
        distance= 31+28+31+30+31+30+31+31+30+31+30
#Here defines another virbration'Distance':it refers the number of the day in a whole year.For January 1st,Distance =1.
Distance = distance + day
print(days_of_the_whole_year-Distance)
