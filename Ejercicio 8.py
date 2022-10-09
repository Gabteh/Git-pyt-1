Nota_1 = float(input("ingrese la primera nota"))
Nota_2 = float(input("ingrese la segunda nota"))
Nota_3 = float(input("ingrese la tercera nota"))
if Nota_1 > Nota_2 and Nota_1 > Nota_3:
  print("La nota uno  es la mas alta")
elif Nota_2 > Nota_1 and Nota_2 > Nota_3:
  print("La nota dos  es la mas alta")
elif Nota_3 > Nota_2 and Nota_3 > Nota_1:
  print("La nota tres es la mas alta")
elif Nota_1 < Nota_2 and Nota_1 < Nota_3:
  print("La nota uno  es la mas baja")
elif Nota_2 < Nota_1 and Nota_2 < Nota_3:
  print("La nota dos  es la mas baja")
elif Nota_3 > Nota_2 and Nota_3 > Nota_1:
  print("La nota tres  es la mas baja")
else:
    print("ERROR!")
