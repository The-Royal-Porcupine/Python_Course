import csv

# а можно как-то прочитать заголовки столбцов, не переписывая
# их отдельно в список филдз, а сразу?
rows = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
       ]

with open('guys.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)