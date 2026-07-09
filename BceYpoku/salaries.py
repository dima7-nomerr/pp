import random
salaris = []
salaris_count= 10
 
for i in range(salaris_count):
    salaris.append(random.randint(30, 150))
print(salaris)
s=0
for i in range(salaris_count):
    s+=salaris[i]
print(s)

avg = s/ salaris_count
print(avg)
  


#i2s= False
#f=0
#while i2s == False:
    #i2s=True
    #for i in range(salaris_count-1-f):
        #if salaris[i+1]<salaris[i]:
          #  r=salaris[i]
          #  salaris[i]=salaris[i+1]
          #  salaris[i+1]=r
          #  i2s=False
    #f+=1
#print(salaris)        





in3 = 0
m = 00
t = 0
for i in range(salaris_count-1):
    in3 = i
    m = salaris[i]
    for j in range(i+1, salaris_count):
        if salaris[j]<m:
            m = salaris[j]
            in3 = j
    t == salaris[i]
    salaris[i] = salaris[in3]
    salaris[in3] = t

    