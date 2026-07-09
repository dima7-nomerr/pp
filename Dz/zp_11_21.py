rain=[]
count= 31
total = 0
for i in range(count):
    rain[i]= int(input(f"input tain for {i+1} day: "))
print(rain)
for i in range(count):
    total+=rain[i]
print(total)    