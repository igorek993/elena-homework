#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

pi = 3.1415926
radius_squared = radius ** 2
area_of_circle = pi*radius_squared
print("Area of circle is ", area_of_circle)
y=round(5541.7693464,4)
print(y)

#согласно формуле S=pi*(42**2) S=5541.7693464 это и есть площадь искомого круга.
#согласно формуле S=pi*(42**2) площадь искомого круга после округления составляет S=5541.7693


# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

print(23**2+34**2<=42**2)
#point_1 при расчете этой точки по формуле x^2 + y^2 <= R^2 ответ оказался - true
#true

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
print(30**2+30**2<=42**2)
#point_2 при расчете этой точки по формуле x^2 + y^2 <= R^2 ответ оказался - false
#false




# Пример вывода на консоль:
#
# 77777.7777
# False
# False



