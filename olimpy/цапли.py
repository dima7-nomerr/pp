a, b=map(int, input().split())
min_herons= max((a+1)// 2, (b+1)//2)
max_herons= min(a,b)
print(min_herons, max_herons)