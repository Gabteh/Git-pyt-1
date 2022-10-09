op_1 = float(input("ingrese 1 si quiere comvertir de centigrados"
                   "a fahrenheit y 2 en caso contrario"))
if op_1==1:
 Tem = float(input("ingrese la temperatura en grados centigrados"))
 Cen = (Tem * 9/5) + 32
 print("la temperatura en fahrenheit es" + str(Cen))
elif op_1==2:
 Tem_2 = float(input("ingrese la temperatura en grados fahrenheit"))
 Fah = (Tem_2  - 32) * 5/9
 print("La temperatura en centigrados es" + str(Fah))
else: 
    print("ERROR!")
 
