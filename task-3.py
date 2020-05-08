
"""n = int(input('Введите число от 0 до 9'))
#nn = n * 11
#nn = n * 111
#print(n + nn + nnn)
# наверное самый примитивный вариант"""

n = int(input('Введите число от 0 до 9'))
temp = str(n)
sum_1 = temp + temp
sum_2 = temp + temp + temp
sum_1_int = int(sum_1)
sum_2_int = int(sum_2)
total = n + sum_1_int + sum_2_int
print(total)
