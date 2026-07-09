a=int(input())
if a%100==0:
    if a%400==0:
        print("высокосный")
    else:
        print("невысокосный")
elif a%4==0:
    print("высокосный")
else:
    print("невысокосный")