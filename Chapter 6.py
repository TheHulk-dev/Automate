#! python3

# Table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    nbListes = len(table)
    maxLongueurTable = []
    nbEléments = len(table[0])

    for i in range(nbListes-1):
        maxLongueur = 0
        for j in range(nbEléments):
            longueurElément = len(table[i][j])
            if longueurElément > maxLongueur:
                maxLongueur = longueurElément
        maxLongueurTable.append(maxLongueur)
    maxLongueurTable.append(0)

    for j in range(nbEléments):
        for i in range(nbListes):
            print(table[i][j].ljust(maxLongueurTable[i]+5), end='')
        print()


printTable(tableData)
