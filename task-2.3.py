month_num = int(input('Введите номер месяца '))
while 1 > month_num or month_num > 12 :# условие или  допиши
    print("Должно быть в диапозоне от 1 до 12")
    month_num = int(input('Введите номер месяца '))
month_list = ['winter','spring','summer','autumn' ]
month_dict = { 1 : 'winter', 2:'spring', 3:'summer',4:'autumn'}
if month_num == 12 or month_num == 1 or month_num ==2:
    print(month_list[0])
    print(month_dict.get(1))
elif month_num == 3 or month_num == 4 or month_num ==5:
    print(month_list[1])
    print(month_dict.get(2))
elif month_num == 6 or month_num == 7 or month_num ==8:
    print(month_list[2])
    print(month_dict.get(3))
elif month_num == 9 or month_num == 10 or month_num ==11:
    print(month_list[3])
    print(month_dict.get(4))
#winter = [12,1,2,]
#spring = [3,5,4]
#summer = [6,8,7]
#autumn = [9, 10, 11]