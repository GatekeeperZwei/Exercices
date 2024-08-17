print("Programme pour calculer la moyenne d'un élève,\nla moyenne de plusieurs élèves et ensuite\nla moyenne de la classe")
KeynoteM = int(input("1 pour calculer la moyenne de la classe,\n0 pour calculer la moyenne d'un élève: "))
MoyenneCSommes = 0
MoyenneCNb = 0
while KeynoteM == 1:
    Keynote = int(input("1 pour entrer une note,\n0 pour calculer la moyenne: "))
    Nbnotes = 0
    Sommes = 0
    while Keynote == 1:
        x = 0
        x = int(input("Note: "))
        Nbnotes = Nbnotes +1
        Sommes = Sommes + x
        Keynote = 0
        Keynote = int(input("Continuer: "))
    else:
        Moyenne = Sommes / Nbnotes
        print("La moyenne de l'élève' est: ")
        print(Moyenne)
        MoyenneCSommes = MoyenneCSommes + Moyenne
        MoyenneCNb = MoyenneCNb + 1
        Moyenne = 0
        KeynoteM = 0
        KeynoteM = int(input("1 pour calculer une autre moyenne d'élève,\n0 pour calculer la moyenne de la classe: "))
else:
    MoyenneC = MoyenneCSommes / MoyenneCNb
    print("La moyenne de la classe est : ")
    print(MoyenneC)
