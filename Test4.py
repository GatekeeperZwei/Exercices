from statistics import mean
# note : variable.pop = variable.remove : pour effacer un element en particulier
# note : del.variable[pour effacer dans la liste]
# note : variable.clear pour nettoyer toute la liste
# note : variable.append pour ajouter un mot dans la liste
# note : variable.extend pour etendre la liste actuelle avec d'autre(s) élément(s)
# import pour importer un module, from [module] import [fonction] pour utiliser une fonction unique d'un module
# mean pour faire une moyenne

# Générateur de phrases
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4/..."
# transformer cette chaine en une liste
# la melanger
# si le nombre d'elements de cette liste est inferieur  à 10
# -> afficher les deux premiers mots
# si le nombre d'elements de cette liste est superieur à 10
# -> afficher les trois derniers
# print(liste_de_mots[len(liste_de_mots) - 1], liste_de_mots[len(liste_de_mots) - 2], liste_de_mots[len(liste_de_mots) - 3])
# print(liste_de_mots[:2])

from random import shuffle
confirmation = 0
liste_de_mots = [""]
liste_de_mots.clear()
while confirmation == 0:
    liste_de_mots.append(input("Entrer un mot: "))
    confirmation += 1
    question_confirmation = input("Souhaitez-vous insérer plus de mots ? (y, n) ")
    if question_confirmation == "y":
        confirmation -= 1
    else:
        shuffle(liste_de_mots)
        if len(liste_de_mots) < 10:
            print(liste_de_mots)
            print(liste_de_mots[:2])
        elif len(liste_de_mots) > 10:
            print(liste_de_mots)
            print(liste_de_mots[len(liste_de_mots) - 3:])
