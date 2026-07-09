n, i, j=map(int, input().split())
if n-j > j-i:
    e=j-i-1
    print(e)
elif n-j < j-i:
    e=n-j-i-1
    print(e)