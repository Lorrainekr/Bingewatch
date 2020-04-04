# -*-coding:utf-8 *

import os
from random import randrange  # importation du module de génération aléatoire
from math import ceil  # permet d'arrondir un chiffre pour qu'il soit toujour entier
import test

"""Faire un petit programme de sélection de série à regarder"""
# mon algorithme :

# faire un programme qui choisit une série de façon aléatoire
# prendre en compte le nombre de série à choisir
# hemlock grove, peaky blinders, the boys, preacher, happy
# message qui t'invite a lancer la roue de sélection

# une boucle pour sortir un chiffre random entre 1 et 5

# sortir directement le nom de la série
# chaque série correspond a un nombre
# créer une liste de série allant de 0 a 4

### DEBUT DU CODE ###

# Création d'un input qui invite à lancer le programme
tv_series = ["Hemlock Grove", "Peaky Blinder", "The Boys", "Preacher", "Happy" ]
start_roulette = input("Vous ne savez pas quelle série choisr ? Je vais vous aider ! taper ENTER pour lancer bingewatch !")

random_number = randrange(60)

def series_roulette():
    if random_number >= 10 and random_number < 20 :
        print("Ce soir c'est : ",tv_series[0])
        return random_number
    elif random_number >= 20 and random_number < 30:
        print("Ce soir c'est : ",tv_series[1])
        return random_number
    elif random_number >= 30 and random_number < 40:
        print("Ce soir c'est : ",tv_series[2])
        return random_number
    elif random_number >= 40 and random_number < 50:
        print("Ce soir c'est : ",tv_series[3])
        return random_number
    elif random_number >= 50 and random_number < 60:
        print("Ce soir c'est : ",tv_series[4])
        return random_number
    else:
        pass

series_roulette()
print("Bon bingewatch !")
