#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)

sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99},
    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99},
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}


cookies_item = sweets['печенье'][1]
cookies_price = cookies_item['price']
cookies_shop = cookies_item['shop']
print('печенье - стоимость', cookies_price, 'шт.', 'магазин', cookies_shop)

candy_item = sweets['конфеты'][2]
candy_price = candy_item['price']
candy_shop = candy_item['shop']
print('конфеты - стоимость', candy_price, 'шт.', 'магазин', candy_shop)

caramel_item = sweets['карамель'][2]
caramel_price = caramel_item['price']
caramel_shop = caramel_item['shop']
print('карамель - стоимость', caramel_price, 'шт.', 'магазин', caramel_shop)

tart_item = sweets['пирожное'][1]
tart_price = tart_item['price']
tart_shop = tart_item['shop']
print('пирожное - стоимость', tart_price, 'шт.', 'магазин', tart_shop)
