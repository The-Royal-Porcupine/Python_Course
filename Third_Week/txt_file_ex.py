
with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(len(content))
    words = content.split()
    print(len(words))
    print(content)

with open('referat2.txt', 'w', encoding='utf-8') as f1:
    new_content = content.replace('.', '!')
    f1.write(new_content)

