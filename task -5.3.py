with open("empl.txt","r") as job:
    poor= []
    sal = []
    money = []
    job_f = job.read().split('\n')
    for i in job_f:
        i = i.split()
        b = float(i[1])

        if b < 20000:
            poor.append(i[0])
            money.append(i[1])
        else:
            sal.append(i[0])
            money.append(i[1])
    sum_b = float(money[0]) +float(money[1])+float(money[2])
    print(round(sum_b))
    print(f'Оклад меньше 20.000 {poor} средний оклад сотрудников  {round(sum_b/3)}')


