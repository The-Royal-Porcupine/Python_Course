def format_price(price):
    price = int(float(price))
    return str('Цена: ' + str(price) + ' руб.')

if __name__ == "__main__":
    price = input()
    print(format_price(price))