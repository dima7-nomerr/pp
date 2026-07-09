def r(n):
    
    print(n,end="")

    n+=1
    
    
    if n<10:
        
        r(n)
    print(n,end="")
    print()

r(0)