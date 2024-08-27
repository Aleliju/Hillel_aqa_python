adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Amount of h:", adwentures_of_tom_sawer.find("h"))


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
separate_words = adwentures_of_tom_sawer.split()
count = 0

for word in separate_words:
    if word.startswith(tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
        count += 1

print("Amount of upper letters:", count)



# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("Place of Tom:", adwentures_of_tom_sawer.find("Tom", 1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None  # Если я правильно понимаю то это инициализация переменной и ее можно не использовать, а то на нее ругается PEP 8
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print("Split sentences", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Forth sentense:", adwentures_of_tom_sawer_sentences[3])
print("Lower registr:", adwentures_of_tom_sawer_sentences[3].strip().lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Found a sentence that starts with 'By the time':", sentence.strip())

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Amount of words in the last sentence:", len(adwentures_of_tom_sawer_sentences[-2].strip().split()))
