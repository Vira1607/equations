print('Уравнение')

# Даны действительные коэффициенты a, b, c,
# при этом a≠0. 
# Программа решает квадратное уравнение ax^2+bx+c=0
# и выводит все его корни.
# 
# Если уравнение имеет два корня,
# выведится два корня в порядке возрастания,
# если один корень — одно число,
# если нет корней — не выводится ничего

import math

print('ax^2+bx+c=0')

a = float(input('Коэффициент a: '))
b = float(input('Коэффициент b: '))
c = float(input('Коэффициент c: '))

discriminant = b ** 2 - 4 * a * c

root_first = (- b - math.sqrt(abs(discriminant))) / (2 * a)
root_two = (- b + math.sqrt(abs(discriminant))) / (2 * a)

if (discriminant >= 0):
  print(max(root_first, root_two))
  if (discriminant != 0):
    print(min(root_first, root_two))
