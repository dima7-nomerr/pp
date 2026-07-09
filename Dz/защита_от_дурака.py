lift=1
right=100
user=0
is_cor=False
while is_cor == False:
    user=int(input(f"введите от {lift} до {right}"))
    if user >= lift and user<=right:
        is_cor=True
    else:
        print(f"Ошибка ввода. Граници должны быть от {lift} до {right}")
