from Fishs import Fish
from fish_functions import *
prodykt= []
kypul = []
porol=3455

l=vvod_porol(porol)
user_state=-1
is_running= True
while is_running==True:
    if l == "no":
        user_state=market()
    elif l == "klys":
        is_running= -1


        

    if user_state == 1:
        ID = proverka_na_int("Введи id: ")
        fisshi=id_poisk(ID, prodykt)
        print_id_fish(fisshi)

        print("напиши 1 если хочешь купить")
        print("напиши 0 если хочешь выйти")
        state=stoto_tam_po_id2()
        input("нажмите enter для продолжения ")

        if state == 1:
            kypul.append(fisshi)
            pop_id_fish(fisshi, prodykt)
            print("вы купили продукт")
            print()

        elif state == 0:
            pass
    elif user_state == 2:
        print_prodyktov(prodykt)

    elif user_state == 3:
        pravelinye_slova="большой | средний | маленький"
        suda=("напиши сюда нужный размер ")
        nuzhnyy_razmer=proverka_na_str(suda, pravelinye_slova)
        print_po_razmery(nuzhnyy_razmer, prodykt)
        input("нажмите enter для продолжения ")

    elif user_state == 4:
        pravelinye_slova='рыба | икра | водоросль'
        suda=("напиши сюда нужное название продукта ")
        mazvanie_prodykta=proverka_na_str(suda, pravelinye_slova)
        print_po_mazvanie_prodykta(mazvanie_prodykta, prodykt)
        input("нажмите enter для продолжения ")

    elif user_state == 5:
        pravelinye_slova="парной | свежий | замороженый"
        suda=("введите способ приготовления ")
        nuzhnyy_prigotovlenie=proverka_na_str(suda, pravelinye_slova)
        print_po_prigotovlenie(nuzhnyy_prigotovlenie, prodykt)
        input("нажмите enter для продолжения ")

    elif user_state == 6:

        summa(prodykt)
        input("нажмите enter для продолжения  ")

    elif user_state == 7:
        l=vvod_porol(porol)
        if l == "klys":
            pass

    elif user_state == 8:
            file_neim=file_neim_vvod()
            save_to_file_for_print(file_neim, prodykt)
            print("файл записан")

    elif user_state == 0:
        print("это всё что вы купили")
        print(kypul)
        break

    while l=="klys":
        admin_state= menu()

        if admin_state == 1:
            new_fish=input_fish_market()
            new_fish.id=id_fish()
            input_prodykt_B_list(prodykt, new_fish)
            input("нажмите enter для продолжения ")
            

        elif admin_state == 2:
            ID = proverka_na_int("Введи id: ")
            fisshi=id_poisk(ID, prodykt)
            print_id_fish(fisshi)
            print("напиши 1 если хочешь удалить")
            print("напиши 2 если хочешь изменить")
            print("напиши 3 если хочешь купить")
            print("напиши 0 если хочешь выйти")
            admin_stat=stoto_tam_po_id()
            input("нажмите enter для продолжения ")

            if admin_stat == 1:
                pop_id_fish(fisshi, prodykt)
                print()
            elif admin_stat == 2:
                pop_id_fish(fisshi, prodykt)
                updeit_po_id(fisshi)
                input_prodykt_B_list(prodykt, new_fish)
                print()
            elif admin_stat ==3:
                
                kypul.append(fisshi)
                pop_id_fish(fisshi, prodykt)
                print("вы купили продукт")
                print()
            elif admin_stat == 0:
                pass
        elif admin_state == 3:
            print_prodyktov(prodykt)

        elif admin_state == 4:
            pravelinye_slova="большой | средний | маленький"
            suda=("напиши сюда нужный размер ")
            nuzhnyy_razmer=proverka_na_str(suda, pravelinye_slova)
            print_po_razmery(nuzhnyy_razmer, prodykt)
            input("нажмите enter для продолжения ")

        elif admin_state == 5:
            pravelinye_slova='рыба | икра | водоросль'
            suda=("напиши сюда нужное название продукта ")
            mazvanie_prodykta=proverka_na_str(suda, pravelinye_slova)
            print_po_mazvanie_prodykta(mazvanie_prodykta, prodykt)
            input("нажмите enter для продолжения ")

        elif admin_state == 6:
            pravelinye_slova="парной | свежий | замороженый"
            suda=("введите способ приготовления ")
            nuzhnyy_prigotovlenie=proverka_na_str(suda, pravelinye_slova)
            print_po_prigotovlenie(nuzhnyy_prigotovlenie, prodykt)
            input("нажмите enter для продолжения ")

        elif admin_state == 7:

            summa(prodykt)
            input("нажмите enter для продолжения ")

        elif admin_state == 8:
            porol=new_porol()


        elif admin_state == 9:
            l=vvod_porol(porol)
            if l == "no":
                pass

        elif admin_state == 10:
            file_neim=file_neim_vvod()
            save_to_file_for_print(file_neim, prodykt)
            print("файл записан")

        elif admin_state == 11:
            save_to_file_to_upload(prodykt)
            print("файл записан")


        elif admin_state == 0:
            print("это всё что вы купили")
            print(kypul)
            is_running= False




