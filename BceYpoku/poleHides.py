COMP_GENERATED_QUESTIONS = [
    "Какой фрукт обычно жёлтого цвета?",
    "Какое животное говорит мяу?",
    "Как называется столица России?",
    "Какой напиток делают из листьев чайного куста?",
    "Как называется планета, на которой мы живём?",
    "Какое время года идёт после зимы?",
    "Какой предмет нужен, чтобы писать?",
    "Как называется большой водоём с солёной водой?",
    "Какой день недели идёт после понедельника?",
    "Как называется дом для птиц?",
]

COMP_GENERATED_ANSWERS = [
    "банан",
    "кошка",
    "москва",
    "чай",
    "земля",
    "весна",
    "ручка",
    "море",
    "вторник",
    "гнездо",
]

CLOSED_LETTER="⬛"

question= ""
answer= ""
guess_answer=""
e="y"
while e=="y":
    input_type = int(input("выберите спопоб ответв 1 выбравть в ручную 2 выбрать из готовых вариантов"))

    if input_type == 1:
        question = input("введите свой вопрос ")
        answer = input("введите слово")
    elif input_type == 2:
        for i in range(len(COMP_GENERATED_ANSWERS)):
            print(f"Пара вопрос-ответ №{i+1}")
            print(f"{COMP_GENERATED_QUESTIONS[i]} - {COMP_GENERATED_ANSWERS[i]}")
        plair_index = int(input("введи номер пары"))-1
        question = COMP_GENERATED_QUESTIONS[plair_index]
        answer = COMP_GENERATED_ANSWERS[plair_index]

    guess_answer = CLOSED_LETTER * len(answer)


    is_run = True

    while is_run == True:
        print(f"Вопрос {question}")
        print(f"Отгаданое слово {guess_answer}")
        print("=="*20)
        input_type = int(input("выберите спопоб ответа 1 ввести букву 2 ввести слово"))

        if input_type == 1:
            input_letter = input("Введите букву")
            for i in range(len(answer)):

                if input_letter == answer[i]:
                    guess_answer = guess_answer[:i]+ input_letter + guess_answer[i:] 
                    is_guees_letter = True  
                
                if is_guees_letter == True:
                    print("выша буква есть")
                else:
                    print("ввашей буквы нету")


        elif input_type == 2:
            input_letter = input("Введите слово")
            input_word = input("введите сло теликом ")
            if input_word == answer:
                guess_answer= answer
                print("вы угадали всё слово")
                break
            else:
                print("вы ввели не верное слово")

        if guess_answer == answer:
            print("вы угодали урааааа")
            is_run = False
    r=int(input("хотите поиграть ещё 1-да 2-нет"))
    if r== 1 :
        r="y"
    else:
        r="n"

