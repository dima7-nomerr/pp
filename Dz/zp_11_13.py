import random
array = []
c= 0
c= random.randint(5, 15)
for i in range(c):
    cu = int(input(f"введите {i+1} из {c} заначение"))
    array.append(cu)

for i in range(c):
    print(array[i], end=" ")
r=int(input(f"ввелите требуемый индекс длч вывода (от 0 до {c-1}):  "))
if r>=0 and r<= r-1
    print(array[r])
else:
    print('нет индекс в массиве')

