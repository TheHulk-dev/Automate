#! python3

# Fantasy game inventory

monInventaire = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayinventory(inventaire):
    nbItems = 0
    print('Inventaire :')
    for k, v in inventaire.items():
        nbItems += v
        print(f'{v} {k}')
    print('Nombre total d\'éléments : %s' % nbItems)

def addToInventory(inventaire, objetsAjoutés):
    pass

displayinventory(monInventaire)
