#Программа принимает действительное положительное число x
#и целое отрицательное число y. Необходимо выполнить возведение
#числа x в степень y. Задание необходимо реализовать в виде функции
#my_func(x, y). При решении задания необходимо обойтись без встроенной
#функции возведения числа в степень.


x = int(input("enter real positive number X"))
if x <= 0:
    x = int(input("enter real positive number X"))

y = int(input("Enter negative integer Y "))
if y >= 0:
    y = int(input("Enter negative integer Y "))
def my_func(x,y):
    return round(x ** y, 3)
print(my_func(x,y))

