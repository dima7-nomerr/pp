god=int(input())
if god%400==0 or (god%4==0 and god%100!=0):
    print("12/09/"+str(god))
else:
    print("13/09/"+str(god))