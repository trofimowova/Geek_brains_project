def big_summ (num_1,num_2,num_3):
    if num_1 >= num_2 and num_3 >= num_2:
        return num_1 + num_3
    elif num_1 >= num_3 and num_2 >= num_3:
        return num_1 + num_2
    else:
        return num_2 +num_3
print(f' Result is {big_summ(int(input("Enter num 1")),int(input("Enter num 2")),int(input("Enter num 3")))}')
