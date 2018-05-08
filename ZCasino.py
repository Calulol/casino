import os
from random import choice
from math import ceil

i=0
list=[]
while i<50:
    list.append(i+1)
    i=i+1
num = choice(list)
parite1 = num%2==0

choix=0
while choix<1 or choix>50:
    print("Il faut choisir un numméro entre 1 et 50")
    choix=int(input("Quel est votre choix ? "))
    
Mise=int(input("Quel est votre Mise ? "))

parite2=choix%2==0
print("Résultat de la roulette :", num)

if choix==num:
    print("Bravo vous avez gagné !")
    gain=3*ceil(Mise)
elif parite1==parite2:
    print("Bravo vous êtes sur la bonne couleur !")
    gain=ceil(Mise/2)
else:
    print("Perdu ...")
    gain=0
print("Vos gains : ", gain)