print("Сейчас произведем некоторые расчеты")
revenue = int(input("Ввведите сумму выручки вашей фирмы"))
costs = int(input("Введите сумму издержек фирмы"))
profit = (revenue - costs)
profitability = profit / revenue *100
if revenue > costs:
    print("Фирма работает в прибыль")
    print("Рентабельность выручки составляет" , round(profitability) , " % ")
    empl_num = int(input(" Введите количесвто сотрудников в вашей фирме "))
    empl_value = profit / empl_num
    print("Прибыль на 1 сотрудника  составляет : " , round(empl_value))
else:
    print("Фирма работает в убыток")
