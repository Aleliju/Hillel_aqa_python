alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = """
'"Would you tell me, please, which way I ought to go from here?"
\n"That depends a good deal on where you want to get to," said the Cat.
\n"I don't much care where ——" said Alice.
\n"Then it doesn't matter which way you go," said the Cat.
\n"—— so long as I get somewhere," Alice added as an explanation.
\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
"""

# task 02 == Знайдіть та єкранізуйте всі символи одинарної лапки (') у тексті
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'


# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
are_of_Black_sea = 436402
are_of_Azov_sea = 37800
sum_of_are_Black_and_Azov_sea = are_of_Black_sea + are_of_Azov_sea
print("Sum of are Black and Azov sea:", sum_of_are_Black_and_Azov_sea)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_sum = 375291
sum_of_goods_first_and_second_warehouse = 250449
sum_of_goods_second_and_third_warehouse = 222950
first_warehouse = sum_of_goods_first_and_second_warehouse + sum_of_goods_second_and_third_warehouse - total_sum
second_warehouse = sum_of_goods_first_and_second_warehouse - first_warehouse
third_warehouse = sum_of_goods_second_and_third_warehouse - second_warehouse
print("First warehouse:", first_warehouse)
print("Second warehouse:", second_warehouse)
print("Third warehouse:", third_warehouse)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
period = 18
one_pay = 1179
sum_of_pay = one_pay * period
print("Sum of pay:", sum_of_pay)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 / 8
b = 9907 / 9
c = 2789 / 5
d = 7248 / 6
e = 7128 / 5
f = 19224 / 9
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_big = 4 * 274
pizza_small = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_coast = pizza_big + pizza_small + juice + cake +water
print("Total coast:", total_coast)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos = 232
total_photos_on_one_page = 8
total_pages = total_photos / total_photos_on_one_page
print("Total pages:", total_pages)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_consumption = 9 / 100
tank_capacity = 48
need_fuel = distance * fuel_consumption
print("Need fuel:", need_fuel)
times_refuel = need_fuel / tank_capacity
print("Times refuel:", times_refuel)

