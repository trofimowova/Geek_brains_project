"""n = int(input('Введите  число'))
s = n%10
n =  n // 10
while n%10 > s and n > 0:
     s = n%10
     n = n // 10
     if s > n%10:
          print(s , "не то")

print("Самое большое число" , s)
# теперь работает только в случае соблюдения последовательностей
"""

num = int(input("введите число"))
print(num)

strNum = str(num)
maxDigit = -1

for ex in range(len(strNum)):
    if strNum[ex] == '.':
        continue
    elif maxDigit < int(strNum[ex]):
        maxDigit = int(strNum[ex])

print(maxDigit)