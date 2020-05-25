
with open("03.txt",'w') as file:
    a = 0
    while True:
            a = input("Введите слово\n")
            file.writelines(a)
            if a =="":
                break


