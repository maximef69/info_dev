print("Entrer les valeurs du point A")
xa = float(input("Entrer la température de A : "))
ya = float(input("Entrer la résistance de A : "))
print("Entrer les valeurs du point B ")
xb = float(input("Entrer la température de B : "))
yb = float(input("Entrer la résistance de B : "))
if xb-xa == 0 :
    print("Vérifier les températures saisies (elles ne doivent pas être égale)") #pas de division par 0
    exit()
A = (yb-ya)/(xb-xa)                            #calcul du coefficient directeur
B = ya-A*xa                                    #calcul de l'ordonnée à l'origine
print("La valeur de A =", round(A,2), "La valeur de B =", round(B,2))