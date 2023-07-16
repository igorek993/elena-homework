# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import lion as lion

# есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль
zoo.insert(1, "bear")
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
# и выведите список на консоль
print(zoo+birds)

# уберите слона
# и выведите список на консоль
zoo.remove("elephant")
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
zoo_cells = zoo+birds
lion=zoo_cells.index('lion')+1
lark=zoo_cells.index('lark')

print('лев сидит в', lion,'й клетке')
print('жаворонок сидит в',lark,'й клетке')


