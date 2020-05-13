
list_count = int(input('Введите количество элементов в списке'))
my_list = []
i = 0
ex = 0
while i < list_count:
    my_list.append(input("Введите значение списка"))
    i = i + 1

for deus in range(int(len(my_list)/2)):
    my_list[ex],my_list[ex+1]=my_list[ex+1],my_list[ex]
    ex = ex + 2
print(my_list)
