def name_user():
    global name_us
    name_us = (input('Введите ваше имя:\n'))
    return name_us

def age(name_user):
    a = input('Сколько вам лет? Введите цифрами Ваш возраст:')
    q = True
    # Проверка на правильность ввода целочисленного числа
    while  q == False:
        try:
            int(a)
            q = True
        except ValueError:
            q = False
        a = input('Вы ввели неверный возраст\n или использовали при этом буквы,\n введите сколько вам лет, пожалуйста, снова\n')
    b = int(a)
    if b < 18:
        print('Вы не можете играть с нами, потому что слишком молоды')
    elif b > 80:
        very_old = input('Игра очень утомительная, вы действительно хотите играть?\n (Дв/Нет)').lower()
        q = False
        #Проверка на правильность ввода Да/Нет
        while q == False:
            if very_old.startswith('д') == True:
                print(f'Мы рады с вами познакомиться {name_user}')
            elif very_old.startswith('н') == True:
                print('Досвидания, до новых встреч')
            else:
                print('Вы ошиблись с вводом ответа,\n игра очень утомительная, вы действительно хотите играть?\n (Да/Нет), ')
                very_old = input().lower()
    else:
        print(f'Добро пожаловать в нашу игру {name_user}')


def print_alphabet(name):
    print('Я могу назвать буквы алфавита, которых нет в твоем имени. и Произнести их.')
    a = ord('а')
    alphabet = set([chr(i) for i in range(a, a+33)])
    u = name.lower()
    for char in alphabet:
        if u.count(char) >= 1:
            pass
        else:
            print(char)




name_us = ' '
# создание отдельной переменной для имени игрока,
# иначе не получалось функцию засунуть в ввод словаря query.
query = {
    'name_game' : input('Введите название игры:'),
    'name_user' : name_user(),
    'age_user' : age(name_us),
    'gender_user' : input('Ваш Пол:'),
    'tomagochi_name' : input('Введите имя вашего питомца'),
    'preference_user' : input('Любите ли вы играть? (Да/Нет)'),
}

print_alphabet(query['name_user'])


print('Конец')