a = int(input("Введите ваш начальный километраж пробежек"))
b = int(input("Какого результата вы хотите добиться"))
day = 1
while  b > 100:
    print("Будьте реалистами. Нfчнем с чего попроще")
    b = int(input("Какого результата вы хотите добиться"))
while  a < b:
    print(day, " ый день :", round(a, 2))
    a = (a * 1.1)
    day = day + 1
    if b <= a:
        print(day, " ый день :", round(a, 2))
        break
#print("На ", day, "день спортсмен добился результатов не менее" ,  b  , "километров")
print( f' На  {day} день спортсмен добился результатов не менее  {b}   километров')
#