import random
count_w = int(input())
salaries= []
for _ in range(count_w):
    salaries.append(random.randint(50000, 150000))
for i in range(count_w):
    print(f"Сотрудник № {i+1} зп - {salaries[i]} руб.")    
print("================================")

for i in range(count_w):
    if salaries[i] > 100000:
        print(salaries[i])