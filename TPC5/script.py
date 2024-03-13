# i need a list of products like this: (id | name | price)
# (1, water, 50c) -> 50c = 50 cents
# then there are three possble commands, LISTAR -> lists all products(the complete table)
# MOEDA -> is followed by a bunch of coins like MOEDA 1c 5c 1e (e = euro) and then retuns the Saldo -> MOEDA 1c 5c 1e -> 1e6c
# SELECIONAR -> is followed by the id of the product, SELECIONAR 2, then it will check if you have enough money to buy the product, if you have then it prints the SALDO left, else a message saying you do not have enough money
# SAIR -> when this token is found the current SALDO is printed and then the necessary coins that the machine needs to give to pay that amount is also printed
# all of this needs to be done using ply

import ply.lex as lex
import json
import sys

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'ADICIONAR',
    'SAIR'
)

def t_LISTAR(t):
    r'(?i)LISTAR'
    return t

def t_MOEDA(t):
    r'(?i)MOEDA[ ]+([1c|2c|5c|10c|20c|50c|1e|2e],?)+'
    return t

def t_SELECIONAR(t):
    r'(?i)SELECIONAR[ ]\d+'
    return t

def t_ADICIONAR(t):
    r'(?i)ADICIONAR[ ]\w+[ ]\d+[ ]?(\d+e\d+c|\d+c|\d+e)?'

    return t

def t_SAIR(t):
    r'(?i)SAIR'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def vending_machine(data):
    lexer = lex.lex()
    saldo = 0

    for line in sys.stdin:
        lexer.input(line)
        for tok in lexer:
            if(tok.type == "LISTAR"):
                print('     Number          |            Name                               |       Stock          |    Price    ')
                for id, product in data.items():
                    print(f"        {id: <5}        |        {product['name']: <30}         |        {product['stock']: <5}         |        {product['price']: <5}")

            elif(tok.type == "MOEDA"):
                coins = tok.value.split()[1].split(",")
                for coin in coins:
                    if coin.endswith('e'):
                        saldo += int(coin[:-1]) * 100
                    elif coin.endswith('c'):
                        saldo += int(coin[:-1])
                euros = saldo // 100
                cents = saldo % 100
                print(f"{euros}e{cents:02d}c")

            elif tok.type == "SELECIONAR":
                id = int(tok.value.split()[1])

                if data[id]['stock'] == 0:
                    print("Product not available. Out of stock")
                    continue

                if id not in data:
                    print("Product not available. Invalid Id")
                    continue

                product_price_str = data[id]['price']

                if 'e' in product_price_str:
                    euro_str, cent_str = product_price_str.split('e')
                    cents = int(cent_str[:-1]) if cent_str else 0
                    product_price = int(euro_str) * 100 + cents
                else:
                    product_price = int(product_price_str[:-1])

                if saldo >= product_price:
                    saldo -= product_price
                    # needs to be in the 2e10c format
                    euros = saldo // 100
                    cents = saldo % 100
                    print(f"Change: {euros}e{cents:02d}c")
                    data[id]['stock'] -= 1
                else:
                    print("You do not have enough money")

            elif tok.type == "ADICIONAR":
                # read name and the stock, if the product already exists in the machina then just add the stock, else add the product to the machine
                name = tok.value.split()[1]
                stock = int(tok.value.split()[2])

                #check if the product already exists
                exists = False
                for id, product in data.items():
                    if product['name'] == name:
                        product['stock'] += stock
                        exists = True
                        break
                if not exists:
                    id = len(data) + 1
                    data[id] = {'name': name, 'stock': stock, 'price': tok.value.split()[3]}
                print(f"Product {name} added to the machine")

            elif tok.type == "SAIR":
                # needs to be in the 2e10c format
                euros = saldo // 100
                cents = saldo % 100
                print(f"{euros}e{cents:02d}c")
                change = []
                for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
                    while saldo >= coin:
                        if coin >= 100:
                            change.append(f"{coin//100}e")
                        else:
                            change.append(f"{coin}c")
                        saldo -= coin
                print(" ".join(change))




def main(argv):
    
    if(len(argv) < 2):
        print("Usage: python3 script.py <input_file>")
        return 1
    
    input_file = argv[1]

    with open(input_file, 'r') as file:
        data = json.load(file)

    products = data['products']
    vendingMachine = {product["id"]: product for product in products}

    vending_machine(vendingMachine)

if __name__ == "__main__":
    main(sys.argv)