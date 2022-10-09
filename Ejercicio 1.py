Numero = 3.14159265359
opcion = float(input(" ingresar una opcion 1 para  calcular el volumen y 2 para el diametro..."))
Resultado = 0
cuadro = 0
if opcion==1 :
 radio = float (input("Ingrese el radio..."))
 cuadro = radio * radio 
 altura = float (input("Ingrese la altura..."))
 Resultado = Numero * radio * altura
 print("El volumen del cilidro es:" + str(Resultado))
elif opcion==2 :
        radio = float (input("Ingrese el radio..."))
        altura = float (input("Ingrese la altura..."))
        Resultado = 2 * Numero * radio * (altura + 1)
        print("El area del cilidro es:" + str(Resultado))
else: 
            print("ERROR!")
         