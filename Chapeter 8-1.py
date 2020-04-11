#! python3

# Chapter 8 : Input validation, sandwich maker

import pyinputplus as pyip

bread_type_list = ['wheat', 'white', 'sordough']
protein_type_list = ['chicken', 'turkey', 'ham', 'tofu']
cheese_type_list = ['cheddar', 'Swiss', 'mozzarella']

bread_type = pyip.inputMenu(bread_type_list, lettered=True)
protein_type = pyip.inputMenu(protein_type_list, lettered=True)
with_cheese = pyip.inputYesNo(prompt='Avec du fromage ?')
if with_cheese == 'yes':
    cheese_type = pyip.inputMenu(cheese_type_list, lettered=True)
mayo = pyip.inputYesNo(prompt='Mayo ?')
mustard = pyip.inputYesNo(prompt='Moutarde ?')
lettuce = pyip.inputYesNo(prompt='Laitue ?')
tomato = pyip.inputYesNo(prompt='Tomate ?')
nb_sandwich = pyip.inputInt('Nombre de sandwich ?')

print('Vous voulez '+str(nb_sandwich)+' sandwich avec :')
print('Type de pain : '+bread_type)
print('Type de protéine : '+protein_type)
if with_cheese == 'yes':
    print('Type de fromage : '+cheese_type)
if mayo == 'yes':
    print('Avec mayo')
if mustard == 'yes':
    print('Avec de la moutarde')
if lettuce == 'yes':
    print('Avec de la laitue')
if tomato == 'yes':
    print('Avec de la tomate')