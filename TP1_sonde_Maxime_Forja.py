print("Entrer les valeurs du point A")
xa = float(input("Entrer la température de A"))
ya = float(input("Entrer la résistance de A"))
print("Entrer les valeurs du point B")
xb = float(input("Entrer la température de B"))
yb = float(input("Entrer la résitance de B"))
A = (yb-ya)/(xb-xa)
B = (ya-A*xa)
print(round(A,2),round(B,2))
