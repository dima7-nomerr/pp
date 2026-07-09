import random

CRISS_SYMBOL = "X"
CROSS_SYMBOL = "0"
EMPTY_CELL = "."

SIZE_FIELD = 3
field = []
current_player = ""
winner_player = ""
USER_X_PLAYER = "игрок 1"
USER_0_PLAYER = "Игрок 2"
DROW='ничья'




current_round = 0
is_plaing = 'yes'
while is_plaing == 'yes':
    for i in range(SIZE_FIELD):
        field.append([])
        for j in range(SIZE_FIELD):
            field[i].append(EMPTY_CELL)


    if random.randint(1, 1000) <= 500:
        current_player = USER_X_PLAYER
        print(f"Первым ходит 1 игр X")
    else:
        current_player = USER_0_PLAYER
        print("Первым ходит 2 игрок 0")
        
    is_playing = True

    while is_playing == True:
        current_round +=1
        print(f"раунд {current_round}")
        for i in range(SIZE_FIELD):
            for j in range(SIZE_FIELD):
                if j< SIZE_FIELD - 1:
                    print(f"{field[i][j]:2}|", end="")
                else:
                    print(f"{field[i][j]:2}", end="")
            print()
            if i< SIZE_FIELD -1:
                print("-" * 8)
        
        if current_player == USER_X_PLAYER:
            print("сейчас ходит крестик ")
            i_symbol = int((input("введите номер строки для выстрела: "))) - 1
            j_symbol = int((input("введите номер столбца для выстрела: "))) - 1

            field[i_symbol][j_symbol] = CRISS_SYMBOL
            current_player = USER_0_PLAYER

        elif current_player == USER_0_PLAYER:
            print("сейчас ходит нолик ")
            i_symbol = int((input("введите номер строки для выстрела: "))) - 1
            j_symbol = int((input("введите номер столбца для выстрела: "))) - 1
            current_player = USER_X_PLAYER

            field[i_symbol][j_symbol] = CROSS_SYMBOL

        if (field[0][0] == CRISS_SYMBOL and field[0][1]==CRISS_SYMBOL and field[0][2]==CRISS_SYMBOL) or (field[1][0] == CRISS_SYMBOL and field[1][1]==CRISS_SYMBOL and field[1][2]==CRISS_SYMBOL) or (field[2][0] == CRISS_SYMBOL and field[2][1]==CRISS_SYMBOL and field[2][2]==CRISS_SYMBOL) or (field[0][0] == CRISS_SYMBOL and field[1][0]==CRISS_SYMBOL and field[2][0]==CRISS_SYMBOL) or (field[0][1] == CRISS_SYMBOL and field[1][1]==CRISS_SYMBOL and field[2][1]==CRISS_SYMBOL) or (field[0][2] == CRISS_SYMBOL and field[1][2]==CRISS_SYMBOL and field[2][2]==CRISS_SYMBOL) or (field[0][0] ==CRISS_SYMBOL and field[1][1]==CRISS_SYMBOL and field[2][2]==CRISS_SYMBOL ) or (field[0][2] ==CRISS_SYMBOL and field[1][1]==CRISS_SYMBOL and field[2][0]==CRISS_SYMBOL ):

            winner_player= USER_X_PLAYER
            is_playing= False
        elif (field[0][0] == CROSS_SYMBOL and field[0][1]==CROSS_SYMBOL and field[0][2]==CROSS_SYMBOL) or (field[1][0] == CROSS_SYMBOL and field[1][1]==CROSS_SYMBOL and field[1][2]==CROSS_SYMBOL) or (field[2][0] == CROSS_SYMBOL and field[2][1]==CROSS_SYMBOL and field[2][2]==CROSS_SYMBOL) or (field[0][0] == CROSS_SYMBOL and field[1][0]==CROSS_SYMBOL and field[2][0]==CROSS_SYMBOL) or (field[0][1] == CROSS_SYMBOL and field[1][1]==CROSS_SYMBOL and field[2][1]==CROSS_SYMBOL) or (field[0][2] == CROSS_SYMBOL and field[1][2]==CROSS_SYMBOL and field[2][2]==CROSS_SYMBOL) or (field[0][0] ==CROSS_SYMBOL and field[1][1]==CROSS_SYMBOL and field[2][2]==CROSS_SYMBOL ) or (field[0][2] ==CROSS_SYMBOL and field[1][1]==CROSS_SYMBOL and field[2][0]==CROSS_SYMBOL ):
            winner_player= USER_0_PLAYER
            
            is_playing= False
            
        elif current_round == 9:
            winner_player = DROW
            is_playing= False

    print(f"игра закончена")
    if winner_player == USER_0_PLAYER:
        print("выйграл 0")
    elif winner_player == USER_X_PLAYER:
        print("выйграл X")
    elif winner_player == DROW:
        print("ничья")
    print
    print("==="*20)
    print("зделал prosto_dima")
    is_plaing=input("хочешь играть ещё? yes - да \ no - нет ")

    
    