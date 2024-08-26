
def main():
    # recolter une valeur porte monnaie
    # creer un produit qui aura pour valeur 50
    # afficher la nouvelle valeur du porte monnaie, après son achat

    # Definition du prix du produit
    produit = 50
    # Valeur du porte monnaie
    portemonnaie = int(input("Entrer la valeur du porte monnaie : "))
    # Affiche le prix du produit
    print("Le prix du produit est de 50€")
    # Entrer le nombre de produit(s) desiré(s) à l'achat
    nombreproduit = int(input("Combien de produit(s) voulez vous acheter : "))
    # Calcul de la dépense
    portemonnaie -= 50*nombreproduit
    # Affichage de la dépense et de la valeur restante du porte monnaie
    print("Vous avez dépensé :" + str(50*nombreproduit))
    print("Votre porte monnaie est maintenant de : " + str((portemonnaie)))



    # print("Hello Deez Nuts")
    # print("Deez Nuts")


if __name__ == '__main__':
    main()
