n, i,e, j=map(int, input().split())
w=0
if n+i%2==0:
    w+=1
elif e+j%2==0:
    w+=1
if  w==2:
    print("Yes")
else:
    print("No")