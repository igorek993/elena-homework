#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)

my_family = ['Igor', 'Alice', 'Elena']

# список списков приблизителного роста членов вашей семьи

my_family_height = [['igor', 178], ['alice',60 ], ['elena',164]]
fathers_height =my_family_height[0][1]
print('fathers height is -',fathers_height,'cm')

    # ['имя', рост],
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

igors_height= 178
alices_height=60
elenas_height=164
print('total family height - ', igors_height+alices_height+elenas_height,'cm')

