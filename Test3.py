# Place de cinéma
# récolter l'age de la personne "Quel est votre age?"
# si la personne est mineur -> 7€
# si la personne est majeur -> 12€
# souhaitez-vous ajouter du popcorn ?
# si oui -> +5€
# afficher le prix total à payer

# Début exercice
age_client = int(input("Quel est votre age ? "))
if age_client < 18:
    place_cinema = 7
else:
    place_cinema = 12
print("Votre place sera à {}€".format(place_cinema))
popcorn = int(input("Souhaitez-vous ajouter du popcorn? 1=oui/0=non : "))
if popcorn == 1:
    place_cinema += 5
    print("Votre total est de {}€".format(place_cinema))
else:
    print("Votre total est de {}€".format(place_cinema))