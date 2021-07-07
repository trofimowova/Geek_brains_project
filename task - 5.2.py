with open("xcom.txt",'r') as deus:
    count_str = deus.readlines()
    print(f' Общее количество строк равно, {len(count_str)}')
    for ex in range(len(count_str)):
        print(f'Количество символов в {ex+1} строке  равно х{len(count_str[ex])} ')
with open("xcom.txt",'r') as deus:
    deus = open("xcom.txt",'r')
    for a in deus:
        a = deus.readline().count(" ")
        print(f' количество слов в строке равно  {a+1}')


#выдает только 2 слова из 4-рех , не понять разобраться почему
