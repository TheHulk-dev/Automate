#! python3
# Regex : Date detection, strong password, strip()

import re

testDate = ['31/12/2054', '15/22/1549', '423/8/1010', 'Ceci n\'est pas une date correct',
            '06/05/1975', '31/04/2020', '29/02/2020', '29/02/2021']

testBissectile = [1200, 1589, 1900, 2004, 2020]

testPassword = ['abc', 'abcdefghi', 'ABCDEFGHIJ',
                'abc123456', 'ABC1234567', 'abCD12', 'abcDEF1234']

testTrim = ['**Bonjour*', '   Hello', 'Hola   ',
            '    Hola amigo ! Como estas ?      ']


def convertirDateEn3Nombres(dateEnString):
    dateRegex = re.compile(r'''(
    (0[1-9]|[12][0-9]|3[01])   #jour
    /
    (0[1-9]|1[012])            #mois
    /
    ([12]\d{3})                #année
    )''', re.VERBOSE)

    mo = dateRegex.search(dateEnString)
    if mo == None:
        return False
    else:
        return mo.groups()


def estAnnéeBissectile(année):
    if année % 4 == 0 and (année % 100 != 0 or année % 400 == 0):
        print('C\'est une bonne date')
        return True
    else:
        print('C\'est une mauvaise date')
        return False


def dateValable(dateTuple):
    _, jour, mois, année = dateTuple
    année = int(année)
    if (mois in ('04', '06', '09', '11') and jour == '31') or (mois == '02' and jour in ('30', '31')) or (mois == '02') and (not estAnnéeBissectile(année)) and (jour == '29'):
        return False
    else:
        return True


def est_un_bon_mot_de_passe(mdp):
    lettres_minuscule = re.compile('[a-z]')
    lettres_majuscules = re.compile('[A-Z]')
    chiffres = re.compile(r'\d')
    mo1 = lettres_minuscule.search(mdp)
    mo2 = lettres_majuscules.search(mdp)
    mo3 = chiffres.search(mdp)
    if len(mdp) >= 8 and mo1 != None and mo2 != None and mo3 != None:
        print('C\'est bon')
    else:
        print('C\'est pas bon')


def fonction_trim(phrase, caractère=''):
    if caractère == '':
        trim_regex = re.compile(r'(^\s*)(.*?)(\s*$)')
    else:
        trim_regex = re.compile(f'(^{caractère}*)(.*?)({caractère}*$)')
    mo = trim_regex.search(phrase)
    # print(mo)
    if mo != None:
        print('*'+mo.group(2)+'*')


for i in range(len(testDate)):
    if convertirDateEn3Nombres(testDate[i]) != False:
        print(dateValable(convertirDateEn3Nombres(testDate[i])))
    else:
        print('Ceci n\'est pas une date valable !')

for i in range(len(testPassword)):
    est_un_bon_mot_de_passe(testPassword[i])

for i in range(len(testTrim)):
    fonction_trim(testTrim[i], r'\*')
