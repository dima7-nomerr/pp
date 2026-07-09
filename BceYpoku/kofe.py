repeat_answer = "y"
# Главный цикл программы.
# Пока пользователь хочет оформлять новые заказы, программа продолжает работу.

while repeat_answer == "y":
    # Список названий товаров.
    # Индексы в этом списке совпадают с индексами цен в списке menu_prices.
    menu_names = [
    "Пицца",
    "Бургер",
    "Картошка фри",
    "Салат",
    "Кола",
    "Чай"
    ]
    # Список цен товаров.
    # Например, цена товара menu_names[0] хранится в menu_prices[0].
    menu_prices = [
    450,
    300,
    180,
    220,
    120,
    90
    ]
    # Корзина клиента.
    # Здесь будут храниться выбранные товары.
    cart_names = []
    cart_prices = []
    cart_counts = []
    # Печать приветствия.
    print()
    print("=" * 35)
    print("Добро пожаловать в кафе Python Food!")
    print("=" * 35)
    # Ввод имени клиента.
    customer_name = input("Введите имя клиента: ")
    # Переменная отвечает за процесс выбора товаров.
    # Пока is_ordering == True, пользователь продолжает добавлять товары.
    is_ordering = True
    # Цикл оформления заказа.
    while is_ordering == True:
        # Печать меню.
        print()
        print("Меню:")
        print("-" * 35)
        for i in range(len(menu_names)):
            print(f"{i + 1}. {menu_names[i]} — {menu_prices[i]} руб.")
        print("0. Завершить заказ")
        print("-" * 35)
        # Ввод номера товара с проверкой.
        is_correct_input = False
        choice = 0
    while is_correct_input == False:
        try:
            choice = int(input("Выберите номер товара: "))
            if choice >= 0 and choice <= len(menu_names):
                is_correct_input = True
            else:
                print("Ошибка. Такого пункта меню нет.")
        except:
            print("Ошибка. Нужно ввести число.")
        # Если пользователь ввёл 0, значит он завершает заказ.
        if choice == 0:
            is_ordering = False
        # Иначе пользователь выбрал товар из меню.
        else:
            product_index = choice - 1
        # Ввод количества товара с проверкой.
        is_correct_count = False
        count = 0
        while is_correct_count == False:
            try:
                count = int(input("Введите количество: "))
                if count > 0 and count <= 20:
                    is_correct_count = True
                else:
                    print("Ошибка. Количество должно быть от 1 до 20.")
            except:
                print("Ошибка. Нужно ввести число.")
        # Добавление товара в корзину.
        cart_names.append(menu_names[product_index])
        cart_prices.append(menu_prices[product_index])
        cart_counts.append(count)
        print()
        print(f"Товар '{menu_names[product_index]}' добавлен в заказ.")
        # Если корзина пустая, чек не печатается.
        if len(cart_names) == 0:
            print()
        print("Заказ пустой. Чек не сформирован.")
        # Если в корзине есть товары, считаем заказ.
        else:
        # Подсчёт общей суммы товаров.
        total_price = 0
        for i in range(len(cart_names)):
        total_price += cart_prices[i] * cart_counts[i]
        # Работа с промокодом.
        discount = 0
        print()
        promo_code = input("Введите промокод или нажмите Enter: ")
        if promo_code == "PYTHON":
        discount = 10
        print("Промокод применён. Скидка 10%")
        elif promo_code == "STUDENT":
        discount = 15
        print("Промокод применён. Скидка 15%")
        elif promo_code == "":
        print("Промокод не введён.")
        else:
        print("Такого промокода нет.")
        # Расчёт скидки в рублях.
        discount_sum = total_price * discount // 100
        # Цена после скидки.
        price_after_discount = total_price - discount_sum
        # Выбор способа получения заказа.
        print()
        print("Способ получения заказа:")
        print("1. Забрать в кафе")
        print("2. Доставка")
        delivery_price = 0
        delivery_choice = 0
        is_correct_delivery = False
        while is_correct_delivery == False:
        try:
        delivery_choice = int(input("Выберите способ получения: "))
        if delivery_choice == 1 or delivery_choice == 2:
        is_correct_delivery = True
        else:
        print("Ошибка. Нужно выбрать 1 или 2.")
        except:
        print("Ошибка. Нужно ввести число.")
        # Самовывоз.
        if delivery_choice == 1:
        delivery_type = "Самовывоз"
        delivery_price = 0
        # Доставка.
        else:
        delivery_type = "Доставка"
        if price_after_discount >= 1000:
        delivery_price = 0
        print("Доставка бесплатная, потому что заказ от 1000 руб.")
        else:
        delivery_price = 200
        # Итоговая сумма к оплате.
        final_price = price_after_discount + delivery_price
        # Печать чека.
        print()
        print("=" * 35)
        print("ЧЕК")
        print("=" * 35)
        print(f"Клиент: {customer_name}")
        print(f"Получение: {delivery_type}")
        print()
        print("Состав заказа:")
        print("-" * 35)
        for i in range(len(cart_names)):
        product_sum = cart_prices[i] * cart_counts[i]
        print(f"{cart_names[i]} x {cart_counts[i]} = {product_sum} руб.")
        print("-" * 35)
        print(f"Сумма товаров: {total_price} руб.")
        print(f"Скидка: {discount_sum} руб.")
        print(f"Доставка: {delivery_price} руб.")
        print(f"Итого к оплате: {final_price} руб.")
        print("=" * 35)
        # Проверка подарка для клиента.
        if final_price >= 1500:
        print("Клиент получает подарок: десерт ")
        elif final_price >= 1000:
        print("Клиент получает подарок: купон на скидку ")
        else:
        print("Подарок не выдан.")
        # Запрос на повторный заказ.
        print()
        repeat_answer = input("Оформить новый заказ? (y - да / n - нет): ")
        while repeat_answer != "y" and repeat_answer != "n":
        print("Ошибка. Введите y или n.")
        repeat_answer = input("Оформить новый заказ? (y - да / n - нет): ")
print()
print("Работа кассы завершена.")