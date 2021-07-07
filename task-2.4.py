my_str = input("введите предложение ")
my_blank = []
num = 1
for ex in range(my_str.count(' ') + 1):
    my_blank = my_str.split()
    if len(str(my_blank)) <= 10:
        print(f" {num} {my_blank [ex]}")
        num += 1
    else:
        print(f" {num} {my_blank [ex] [0:10]}")
        num += 1