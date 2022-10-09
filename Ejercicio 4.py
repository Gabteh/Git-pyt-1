from tkinter.tix import INTEGER
Num_1 = int(input("Ingrese un numero"))
Num_2 = Num_1 % 7
if type(Num_1) == INTEGER and Num_2 == 0:
    print ("El numero es entero y multiplo de 7")
elif type(Num_1) == INTEGER and Num_2 >= 1: 
    print ("El numero es entero pero no es multiplo de 7")
else: 
    print ("El numero no es entero y no es multiplo de 7")
