
# # #
ss = int(input('введите время в секундах'))
hours,ss = ss//3600, ss % 3600
minutes = ss// 60
ss = ss % 60
print ( f'{hours} : {minutes} : {ss}')

# Нашел еще такой способ, но как понял для него слишком рано
seconds = int(input('Введите время в секундах'))

import time

def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
print(convert(seconds))