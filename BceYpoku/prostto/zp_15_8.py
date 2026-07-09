

with open("test.txt","r", encoding="utf-8") as file:
    for line in file:
        count_in_cur_line = len(line.strip())

        print(count_in_cur_line)
        




