def ris(x):
    i=0
    gorizantal=int(input(f"сколько символов {x} будет сверху: "))
    
    vertical=int(input(f"сколько символов {x} будет в нис:  "))
    
    while i <=vertical:
        i+=1
        print(x*gorizantal)

      
x=ris(input())
