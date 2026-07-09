n=input()
s=0
for i in n:
    if i=="3":
        s+=1
print(f"в этом числе цифра 3 встречается {s} раза")
s1=0
for i in n:
     if i==n[-1]:
         s1+=1
print(f"в этом числе последняя цифра {s1} раза")
s2=0
for i in n:
    if int(i)%2==0:
        s2+=1
print(f"в этом числе {s2} чётных цифр")
s3=0
for i in n:
    if int(i)>5:
        s3= s3 + int(i)
print(f"в этом числе сумма цифр больших 5 {s3}")
s3=0
for i in n:
    if int(i)>7:
        s3= s3 + int(i)
print(f"в этом числе сумма цифр больших 7 {s3}")
s=0
for i in n:
    if int(i)==0:
        s+=1
    if int(i)==5:
        s+=1
print(f"в этом числе встречаются 5 и 0 {s} раз")
