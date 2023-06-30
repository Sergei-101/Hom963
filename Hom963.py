# Задание №1
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Пример:
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

list_num = [1, 2, 3, 1, 2, 4, 5, 6]
res = []
for i in list_num:
    if list_num.count(i) > 1 and i not in res:
        res.append(i)
print(f"{list_num} ---> {res}")




# Задание №2
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.


text = """Универсальный фиксатор для бровей PÚSY Brow Fix PROFESSIONAL by Илона Дрожь —
это не только женская косметика класса люкс, но и новое слово в beauty индустрии.
Гель для укладки бровей представлен в корпусе двух цветов: белый и черный, составы для ламинирования
бровей и цвет геля одинаковы - прозрачны. Гель пуси имеет в составе своей косметической основы комплекс
 для ухода с витамином В5, ускоряющим рост волос. Для удобства использования средство доставляется в баночке
 объемом 5 мл и с тонкой скошенной щеткой для бровей. Прозрачный гель для бровей незаметен при нанесении,
 обеспечивает длительную фиксацию, питает и укрепляет волосы. Идеальное средство надежно зафиксирует волоски,
 не склеит брови, останется незаметным, не вызовет раздражения и не сушит кожу.
Помада для бровей – уникальное средство на все случаи жизни: благодаря этим свойствам помада способна придавать
 форму бровям. Гель для бровей с эффектом ламинирования сделает их максимально ухоженными. Благодаря нашему
 гелю ваши брови сохранят форму даже после интенсивной тренировки. Уход за бровями также важен, как и любая
 другая бьюти процедура. С помощью геля для оформления, закрепления и супер сильной фиксации контура бровей
 вы получите эффект ламинирования в домашних условиях. Благодаря гелевой текстуре средство для моделирования формы
 бровей легко наносится. Pusy гель для бровей предназначен для профессионального бровиста и визаж - мастера, но его могут
 использовать и обычные женщины для макияжа. Моделирующий, стойкий бесцветный гель фиксатор для бровей и кисточка - щетка
 упакованы в стильную подарочную коробочку станет лучшим подарком. Такой набор для бровей можно взять с собой в путешествие,
 на встречу с подругами. В ассортименте есть средство для бровей в объеме 15 мл и 5 мл. Наш гель фиксатор укладывает даже самые
 густые, жесткие и непослушные брови. В нашем магазине большой выбор косметики для лица и тела, уходовые наборы, бьюти боксы,
 подарочные наборы и другая косметика для лица пуси.У нас есть акции и распродажи, вы можете купить наши товары в подарок со скидкой!"""


for i in text:
    if i in ",.!:-":
        text = text.replace(i, ' ')
text = text.lower().split()
WORD_COUNT = 10
res = {}
for i in text:
    if text.count(i) >= WORD_COUNT:
        res[i] = text.count(i)
print(*res.items())


# Задание №3
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один
# допустимый вариант.
# Верните все возможные варианты комплектации рюкзака.

things = {'зажигалка': 5,
          'компас': 5,
          'фрукты': 200,
          'рубашка': 50,
          'аптечка': 80,
          'куртка': 400,
          'бинокль': 50,
          'удочка': 500,
          'бутерброды': 250,
          'палатка': 800,
          'спальный мешок': 250,
          'жвачка': 5}


def collect_backpack(thing: dict, weight: int) -> dict:
    """
    collects a backpack
    1 - Dict
    2 - weight
    """

    backpack_weight = weight
    res = dict()
    for key, value in thing.items():
        if backpack_weight >= value:
            backpack_weight -= value
            res[key] = value

    return f"Сложили в рюкзак - {res}, Осталось веса {backpack_weight}"

print(f"Первый вариант - {collect_backpack(things, 1000)}")
print(f"Второй вариант - {collect_backpack((dict(sorted(things.items(), key=lambda item: item[1]))), 1000)}")
print(f"Третий вариант - {collect_backpack((dict(sorted(things.items(), key=lambda item: item[1], reverse=True))), 1000)}")

# Задание №4
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
# ** какие вещи взяли все три друга
# ** какие вещи уникальны, есть только у одного друга
# ** какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.


def hike():

    menu = None
    print("1 - Посмотреть список друзей \n2 - Добавить друга \n3 - какие вещи взяли все три друга \n"
          "4 - какие вещи уникальны, есть только у одного друга \n"
          "5 - Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует\n"
          "6 - Выйти")

    baggage = {
        'Denis': ('fishing rod', 'lighter', 'tent'),
        'Alex': ('tent', 'brazier', 'gun'),
        'Vlad': ('tent', 'gun', 'sun cream')
    }

    while menu != 6:
        menu = int(input("Введите комманду - "))
        all_items = list(baggage.values())
        must_have_item = set(all_items[0])
        if menu == 1:
            print(*baggage.items())
        elif menu == 2:
            add_friends = input("Введите им друга - ")
            add_baggage = input("Введите вещи через запятую - ")
            baggage[add_friends] = tuple(add_baggage.split(", "))
        elif menu == 3:
            print(*all_items)
        elif menu == 4:
            uniq_items = {}
            for name, items in baggage.items():
                uniq_items[name] = set(items).difference(must_have_item)
            print(uniq_items)
        elif menu == 5:
            for items in all_items:
                must_have_item = must_have_item.intersection(set(items))
            print(must_have_item)


hike()