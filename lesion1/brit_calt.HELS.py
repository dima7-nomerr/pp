floor=int(input("сколько этажей вы прошли? "))
 
stypenu=int(input("Введите сколько ступенек на пролёте "))

hels=((floor *2)* stypenu)*10
t=hels//60
print("если вы пройдёте ",floor, "этажей то вы повыcети жизнь на ",t ,"минут")
