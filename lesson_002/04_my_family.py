#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)

my_family = ['Igor', 'Alice', 'Elena']

# список списков приблизителного роста членов вашей семьи

my_family_height = [['igor', 178], ['alice', 60], ['elena', 164]]

# ['имя', рост],
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

fathers_height = my_family_height[0][1]
print('fathers height is -', fathers_height, 'cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см


igors_height = my_family_height[0][1]
alices_height = my_family_height[1][1]
elenas_height = my_family_height[2][1]
family_height = igors_height + alices_height + elenas_height
print('total family height - ', family_height, 'cm')
