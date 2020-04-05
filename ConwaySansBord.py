#! python3
import random
import time
import copy

largeur = 20
hauteur = 10

test = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '*', ' ', ' '], [' ', '*', ' ', '*', ' ', ' '],
        [' ', ' ', '*', '*', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]


def creerTableau(largeur, hauteur):
    tableau = []
    for i in range(largeur):
        colonne = []
        for j in range(hauteur):
            if random.randint(0, 1):
                colonne.append('*')
            else:
                colonne.append(' ')
        tableau.append(colonne)
    return tableau


def afficherTableau(tableau):
    for i in range(largeur):
        print('-', end='')
    print()
    for j in range(hauteur):
        for i in range(largeur):
            print(tableau[i][j], end='')
        print()
    for i in range(largeur):
        print('-', end='')
    print()


def caculNouveauTableau(tableau):
    nouveauTableau = copy.deepcopy(tableau)
    for j in range(hauteur):
        for i in range(largeur):
            coordonneeGauche = (i-1)
            coordonneeDroite = (i+1)
            coordonneeHaut = (j-1)
            coordonneeBas = (j+1)
            nbCellulesVivantes = 0
            if coordonneeGauche != -1 and coordonneeHaut != -1:
                if tableau[coordonneeGauche][coordonneeHaut] == '*':
                    nbCellulesVivantes += 1
            if coordonneeGauche != -1:
                if tableau[coordonneeGauche][j] == '*':
                    nbCellulesVivantes += 1
            if coordonneeGauche != -1 and coordonneeBas != hauteur:
                if tableau[coordonneeGauche][coordonneeBas] == '*':
                    nbCellulesVivantes += 1
            if coordonneeHaut != -1:
                if tableau[i][coordonneeHaut] == '*':
                    nbCellulesVivantes += 1
            if coordonneeBas != hauteur:
                if tableau[i][coordonneeBas] == '*':
                    nbCellulesVivantes += 1
            if coordonneeDroite != largeur and coordonneeHaut != -1:
                if tableau[coordonneeDroite][coordonneeHaut] == '*':
                    nbCellulesVivantes += 1
            if coordonneeDroite != largeur:
                if tableau[coordonneeDroite][j] == '*':
                    nbCellulesVivantes += 1
            if coordonneeDroite != largeur and coordonneeBas != hauteur:
                if tableau[coordonneeDroite][coordonneeBas] == '*':
                    nbCellulesVivantes += 1

            if (tableau[i][j] == '*' and nbCellulesVivantes in (2, 3)) or (tableau[i][j] == ' ' and nbCellulesVivantes == 3):
                nouveauTableau[i][j] = '*'
            else:
                nouveauTableau[i][j] = ' '
            #nouveauTableau[i][j] = nbCellulesVivantes
    return(nouveauTableau)


tableau = creerTableau(largeur, hauteur)
while True:
    afficherTableau(tableau)
    tableau = caculNouveauTableau(tableau)
    time.sleep(0.1)
