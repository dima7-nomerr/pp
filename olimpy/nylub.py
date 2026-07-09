n=input()+"1"
t= 0
ter=0
for i in n:
    
    if i=="0":
        t+=1
    elif i=="1":

        
        if t>ter:
            ter=t
        t=0
print(ter)
    

    
