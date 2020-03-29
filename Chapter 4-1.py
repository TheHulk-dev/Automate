def listeEnString(liste):
    phrase = ''
    for nom in liste:
        phrase += nom
        if liste.index(nom) == len(liste)-2:
            phrase += ' and '
        elif liste.index(nom) != len(liste)-1:
            phrase += ', '
    return phrase


test = ['apples', 'bananas', 'tofu', 'cats', 'slime', 'dogs']
print(listeEnString(test))
