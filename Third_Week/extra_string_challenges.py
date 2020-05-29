# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'о', 'у', 'е', 'и', 'ы', 'э', 'ю', 'я']
#print(*map(word.count, vowels))
vowels_count = 0
for letter in word.lower():
    if letter in vowels:
        vowels_count += 1
print(vowels_count)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print(len(sentence)/len(sentence.split()))