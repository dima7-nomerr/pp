i=0
n=100
d=0
t=0
while i<n:
    i+=1
    if i%2!=0:
        d+= 1/i
    else:
        d -= 1/i
    t += 1/i
print(f"дистанция от дома={d:.2f}")
print(f"общая дистаанция={t:.2f}")


    