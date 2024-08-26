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
popcorn_answer = 0
while popcorn_answer == 0:
    popcorn = input("Souhaitez-vous ajouter du popcorn? (Oui, Non) ")
    popcorn_answer += 1
    if popcorn == "Oui":
        place_cinema += 5
        print("Votre total est de {}€".format(place_cinema))
    elif popcorn == "Non":
        print("Votre total est de {}€".format(place_cinema))
    else:
        popcorn_answer -= 1

