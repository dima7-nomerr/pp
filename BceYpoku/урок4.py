import random
print("выбирите уровунь сложности:")
print("1 2 3")
level=int(input())
if level>3:
    print("подошёл и пошёл нахуй")
    left_side = -21324353453
    right_side = 1000000000000000000000000000000000000000000000000000000000000
if level==1:
    left_side=1
    right_side=100
elif level ==2 :
    left_side = 1
    right_side = 500
elif level ==3:
    left_side = 1
    right_side = 1000


comp_number = 0
user_number = 0
tries = 0



comp_number = random.randint(left_side, right_side)

print(f"Я загадал число от {left_side} до {right_side}. Попробуй отгадай")

# print(comp_number)

while user_number != comp_number:
    is_correct_input = False
    tries += 1

    while is_correct_input == False:
        user_number = int(
            input(f"попытка №{tries} - введи число от {left_side} до {right_side}: ")
        )

        if user_number == 1488:
            print(f"введен секретный ключ. загаданное число = {comp_number}")
        elif user_number >= left_side and user_number <= right_side:
            is_correct_input = True
        else:
            print(
                f"ошибка ввода. вы вышли за границы отрезка от {left_side} до {right_side}"
            )

    if user_number < comp_number:
        print("введите число побольше")
        left_side = user_number
    elif user_number > comp_number:
        print("введите число поменьше")
        right_side = user_number


print("поздравляем вы угадали загаданное число")
print(f"вам понадобилось попыток: {tries}")

# if 1 <= tries <= 3:
if tries >= 1 and tries <= 3:
    print("вам тупо повезло")
elif tries >= 4 and tries <= 7:
    print("вы гений")
elif tries >= 8 and tries <= 11:
    print("неплохо")
elif tries >= 12 and tries <= 15:
    print("тренируйся лучше")
else:
    print("сочувствую")
