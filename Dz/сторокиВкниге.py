k, n = map(int, input().split())
s= n%k
st= 0
if n % k==0:
    st= n // k 
else:
    st=n // k +1
print(f"{st} {s}")