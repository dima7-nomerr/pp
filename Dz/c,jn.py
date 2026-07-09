n=int(input())
a=list(map(int,input().split()))
maxsum=0
for i in range(n):
    left=(i-1)%n
    right=(i+1)%n
    cursum=a[i]+a[left]+a[right]
    if cursum>maxsum:
        maxsum=cursum

print(maxsum)