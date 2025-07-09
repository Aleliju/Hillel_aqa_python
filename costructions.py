#TUPLE КОРТЕЖ


# можно считать длину при помощи len
# можно итерироваться при помощи цикла for
# у тапла есть индексы []
# если тапл из одного элемента то обязательна должна быть запятая в конец элемента ("admin",)
#
# распаковка = можно как в кортеже так и в списке
user_role = ("admin", "editor", "creator")
role_1, role_2, role_3 = user_role # и если запринтить то каждая выдаст свой элемент тапла
role_1, role_2, _ = user_role #  если один из элементов не нужен его можно заменить нижним подчеркиванием


#DICT СЛОВАРИ
person = {
    "name": "John",
    "age": 30,
    "city": "Ney York"
}

additional_person = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

# изменять значения
person["job"] = "Engineer"

# вызывать можно по ключу
print(person["name"]) # если запросить не существующий элемент, то будет ошибка для этого есть метод get
print(person.get("name")) # если значения нет, то вернется в таком случае None

# итерирование
for item in person.items(): #будут таплы
    print(item)
for keys, values in person.items(): #будут ключ - значение и при чтении будет по чем происходит итерация
    print(keys, values)
# апдейт словаря другим словарем
person.update(additional_person)
person = person | additional_person # тоже самое что и выше но более удобная конструкция


# *args, **kwargs
def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary

values = [1,2,3,4,5]
other_values = [6,7,8,9,10]

print(add_all(1,2,3,4,5))
print(add_all(*values, *other_values))

def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))

person = {
    "city": "Ney York",
    "age": 30,
    "name": "John",
}

introduce(name="John", age=30, city="Ney York")
introduce(**person)


# JSON
import json

book = {
    'title': '1984',
    'author': 'John',
    'isbn': '978-525484',
    'uuid': '46548-487321564dfg-dfg54dfg-dsf',
}

json_string = json.dumps(book) # convert JSON to str
print(type(json_string))
print(json_string)

json_string2 = '{"title": "1984", "author": "John", "isbn": "978-525484", "uuid": "46548-487321564dfg-dfg54dfg-dsf"}'

book = json.loads(json_string2) # convert JSON to dict
print(type(book))
print(book)

# import

