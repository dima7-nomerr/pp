kolmast=int(input())
d=0
for i in range(kolmast):
    e=list(map(int, input().split()))
    cm=437
    if int(e[0])-cm>0:
        d=i
        break
    elif int(e[0])-cm<0:
        d=3
if d== 3:
    print("No crash")
elif d==1:
    print(f"Crash {d}")
    