name = input('enter name')
surname = input('enter surname')
year = (input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')

def dossier(name, surname, year, city,email,telephone):
    return ''.join([name, surname, year, city,email,telephone])
print(dossier(name, surname, year, city,email,telephone))