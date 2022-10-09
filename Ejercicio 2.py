import math

D_1 = float(input("ingrese el primer cateto"))
D_2 = float(input("ingrese el cateto dos"))
H_1 = math.sqrt((D_1)**2 +(D_2)**2)
print("La primera diagonal es"+ H_1)

A_1 = float(input("ingrese el primer cateto"))
A_2 = float(input("ingrese el cateto dos"))
H_2 = math.sqrt((A_1)**2 +(A_2)**2)
print("La segunda  diagonal es"+ H_2)

if H_1 >H_2:
     print("La diagonal mas grande es" + H_1)
elif H_2 > H_1:
    print("La diagonal mas grande es" + H_2)
 
