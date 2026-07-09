
s=input("введите любой символ с клавиатуры:")
if len(s)<0 or len(s)==0:
    print('ты тупой, веди число нормально')
    exit()
if s>="a" and s<="z" or s>="A" and s<"Z":
    if s>="a" and s<="z":
        print("это маленькая кая англ буква")
    else:
        print("это большаая кая англ буква")    
elif s>="0" and s<="9":
    if int(s)%2==0:
        print("это число чётное")
    else:
        print("ЭТО ЧИСЛО НЕ ЧЁТНОЕ")
else:
    print("это неизвестный символ")
    