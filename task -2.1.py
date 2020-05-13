list = [ ' abc', 123, 1.87, True, [ "a" , False, 456] , ( ' opera', 231) , { 'katalog': 'Saturn' , 'pages': 150 }]
i = 0
for desctibe_type in list:
    desctibe_type = (type(list[i]))
    print(desctibe_type)
    i = i + 1
#print(list.pop())
#print(list)
#list.reverse()
#print(list)
#print(list [0:2])
#print(type(list[0]))
print (len(list))
while len(list)>0:
    print(type(list[-1]))
    list.pop()
    #не знаю как сделать с While и чтобы не обрaтный список был
