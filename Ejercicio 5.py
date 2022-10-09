K_wath = float(input("Ingrese la cantidad de kilowaths"))
Precio_kilowatts = 5.127 
Precio_excedente =  0.1393534002229654
if K_wath < 700:
   cal_1 = K_wath * Precio_kilowatts 
elif K_wath >= 700: 
    cal_2 = K_wath * Precio_kilowatts
    cal_3 = cal_2 * Precio_excedente 
    cal_4 = cal_3 + cal_2
    

