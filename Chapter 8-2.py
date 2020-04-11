#! python3

# Multiplication quiz

import random
import time

import pyinputplus as pyip

nb_questions = 10
nb_essais = 3
temps_réponse = 8
global nb_bonnes_réponses
nb_bonnes_réponses = 0


def une_mutiplication():
    global nb_bonnes_réponses
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    print(f'Combien font {a} * {b}')
    try:
        pyip.inputStr(allowRegexes=['^%s$' % (
            a*b)], blockRegexes=[('.*', 'Incorrect !')], timeout=temps_réponse, limit=nb_essais)
    except pyip.TimeoutException:
        print('Trop lent !')
    except pyip.RetryLimitException:
        print('Trop d\'erreurs')
    else:
        print('Correct !')
        nb_bonnes_réponses += 1


for _ in range(nb_questions):
    une_mutiplication()

time.sleep(1)
print(f'Tu as répondu correctement à {nb_bonnes_réponses} questions sur {nb_questions}')
