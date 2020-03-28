def collatz(number):
    if number % 2 == 0:
        number /= 2
    else:
        number = number*3+1
    return int(number)


BonneEntree = False
while not BonneEntree:
    print('Entrez un nombre entier :')
    try:
        number = int(input())
        BonneEntree = True

    except ValueError as erreur:
        # print(erreur)
        print('Ce n\'est pas un nombre entier !')

while number != 1:
    number = collatz(number)
    print(number)

Daksh = 'C\'est un garçon très mignon'
for c in Daksh:
    print('***'+c+'***')
