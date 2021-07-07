def division (a, b):
    div= a / b
    return div
x = int(input("Enter number one"))
y = int(input("Enter number two"))
if x == 0 or y == 0:
    print("Ноль недопустим")
    x = int(input("Enter number one"))
    y = int(input("Enter number two"))
print(division(x,y))