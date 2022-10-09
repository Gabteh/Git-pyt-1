Lado_1 = float(input("ingrese la primera nota"))
Lado_2 = float(input("ingrese la segunda nota"))
Lado_3 = float(input("ingrese la tercera nota"))
if Lado_1 == Lado_2 and Lado_1 == Lado_3 and Lado_2==Lado_3:
    print("Es un triangulo equilatero")
elif Lado_1 == Lado_2 and Lado_1 != Lado_3 and Lado_2 != Lado_3:
    print("Es un triangulo isoceles")
elif Lado_1 != Lado_2 and Lado_1 != Lado_3 and Lado_2 != Lado_3:
    print ("Es  un triangulo escaleno")