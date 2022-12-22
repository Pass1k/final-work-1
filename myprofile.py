print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')


# Главное меню
def mainMenu():
    while True:
        print('------------------------------------------')
        print('ГЛАВНОЕ МЕНЮ')
        print('1 - Ввести или обновать информацию')
        print('2 - Вывести информацию')
        print('0 - Завершить работу')
        button = int(input('Введите номер пункта меню: '))

        if button == 0:
            break
        elif button == 1:
            updating()
        elif button == 2:
            outputing()


# Функция для вводда информации
def updating():
    while True:
        print('------------------------------------------')
        print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
        print('1 - Личная информация')
        print('2 - Информация о предпринимателе')
        print('0 - Назад')
        button = int(input('Введите номер пункта меню: '))

        if button == 0:
            mainMenu()
        elif button == 1:
            personal_information()
        elif button == 2:
            about_busnissman()


# Фукнция для ввода личной информации updating №1
def personal_information():
    global name, age, phone_number, email, email_index, email_without_index, more_information
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    phone_number = input('Введите номер телефона (+7XXXXXXXXXX): ')
    email = input('Введите адрес электронный почты: ')
    email_index = input('Введите почтовый индекc: ')
    email_without_index = input('Введите почтовый индекс (без индекса): ')
    more_information = input('Введите дополнительную информацию: ')
    updating()


# Функция ввода информации для предприниматели
def about_busnissman():
    global IIN, name_of_the_bank, BIK, correspondent_account

    def ogrnip():
        global Ogrnip
        Ogrnip = input('Введите ОГРНИП: ')
        count = 0

        for i in Ogrnip:
            count += 1

        if count != 15:
            print('ОГРНИП должен содержать 15 цифр')
            Ogrnip = ''
            ogrnip()

    ogrnip()

    IIN = input('Введите ИИН: ')

    def colculation():
        global accounts
        accounts = input('Введите расчетный счет: ')
        count = 0

        for i in accounts:
            count += 1

        if count != 20:
            print('Расчетный счет должен содержать 20 цифр')
            accounts = ''
            colculation()

    colculation()

    name_of_the_bank = input('Введите название банка: ')
    BIK = input('Введите БИК: ')
    correspondent_account = input('Введите корреспондентский счет: ')

    updating()


# Функция чтобы вывести информацию
def outputing():
    while True:
        print('------------------------------------------')
        print('ВЫВЕСТИ ИНФОРМАЦИЮ')
        print('1 - Общая информация')
        print('2 - Вся информация')
        print('0 - Назад')
        button = int(input('Введите номер пункта меню: '))

        if button == 0:
            mainMenu()
        elif button == 1:
            print(f"Имя: {name}")
            print(f"Возраст: {age} лет")
            print(f"Телефон: {phone_number}")
            print(f"E-mail: {email}")
            print(f"Индекс : {email_index}")
            print(f"Адрес: {email_without_index}")
            print(f"Дополнительное информация: {more_information}")

            outputing()
        elif button == 2:
            print(f"Имя: {name}")
            print(f"Возраст: {age} лет")
            print(f"Телефон: {phone_number}")
            print(f"E-mail: {email}")
            print(f"Индекс : {email_index}")
            print(f"Адрес: {email_without_index}")
            print()
            print('Информация о предпринимателе')
            print(f"ОГРНИП: {Ogrnip}")
            print(f"ИИН: {IIN}")
            print(f"Банковскте реквизиты Р/c: {accounts}")
            print(f"Банк: {name_of_the_bank}")
            print(f"БИК: {BIK}")
            print(f"К/c: {correspondent_account}")

            outputing()


mainMenu()