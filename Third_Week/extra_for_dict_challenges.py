from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
# student.values() возвращает "объект словаря". В каких случаях это нужно?
for student in students:
    for k, v in student.items():
        names.append(v)

for item in set(names):
    print(f'{item} : {names.count(item)}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
for student in students:
    for k, v in student.items():
        names.append(v)

# Параметр Ключ что-то делает с очередным итерируемым объектом и возвращает это.
# В данном случае для каждого имени считается кол-во повторений этого имени в списке,
# То есть результат отработки лямбда функции над этим именем

print(f'Самое частое имя среди учеников: {max(names, key=lambda x: names.count(x))}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]

for school_class in school_students:
    names = []
    for student in school_class:
        for k, v in student.items():
            names.append(v)
    print(
        f'Самое частое имя в классе {int(school_students.index(school_class)) + 1}: {max(names, key=lambda x: names.count(x))}')
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for school_class in school:
    boys_count = 0
    girls_count = 0
    for student in school_class['students']:
        for name in student.values():
            if is_male[name]:
                boys_count += 1
            else:
                girls_count += 1
    print(f'В классе {school_class["class"]} {girls_count} девочек и {boys_count} мальчика')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

class_gender = {}
for school_class in school:
    class_gender[school_class['class']] = {'girls_count': 0, 'boys_count': 0}
    for student in school_class['students']:
        for name in student.values():
            if is_male[name]:
                class_gender[school_class['class']]['boys_count'] += 1
            else:
                class_gender[school_class['class']]['girls_count'] += 1
class_max_boys = ''
class_max_girls = ''
max_boys = 0
max_girls = 0
for one_class in class_gender.keys():
    # В for выражение one class типа string, поэтому потом class_gender[one_class], а не просто one_class[]
    if max_boys < class_gender[one_class]['boys_count']:
        max_boys = class_gender[one_class]['boys_count']
        class_max_boys = one_class
    if max_girls < class_gender[one_class]['girls_count']:
        max_girls = class_gender[one_class]['girls_count']
        class_max_girls = one_class
print(f'Больше всего мальчиков в классе {class_max_boys}')
print(f'Больше всего девочек в классе {class_max_girls}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
