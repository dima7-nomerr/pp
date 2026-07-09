n=input()
m=0
max=0
min=0
for i in n:
    if i=="1":
        m+=1
        max+=1
    if i=="2":
        m-=1
        min+=1
if min-max-m<0:
    print((min-max-m+1)*(-1))
else:
    print(min-max-m)
