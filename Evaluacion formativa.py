import os
import time
limpieza_pantalla = "cls"

#Definicion de variables

Pickachu_roll = 4500
Otaku_roll = 5000
PulpoVenenoso_roll = 5200
AnguilaElectrica_roll = 4800
total = 0
descuento = 0 
Respuesta = 0
pedido1 = 0
roll1=0
roll2 = 0
roll3 = 0
roll4 = 0


os.system(limpieza_pantalla)

print("Bienvenido a Sushi Otaku Delivery")
print("A continuacion le mostrare el menu que tenemos disponible")
print("1. Pickachu Roll: $4.500.-\n 2. Otaku Roll: $5.000.-\n 3. Pulpo Venenoso Roll: $5.200.-\n 4. Anguila Electrica: $4.800.-")


while pedido1 == 0:
    time.sleep(1)
    Respuesta= int(input("Seleccione una opcion del menu (1-4)\n"))
    if Respuesta == 1:
        Pickachu_roll= input("Has agregado la opcion Pickachu Roll,¿Cuantos deseas llevar?:\n")
        total = (Pickachu_roll*roll1)
        try: 
            salida = int(input("Deseas agregar otro pikachu roll?\n 1=si)\n 2=no \n "))
            if salida == 1:
                pedido1 = 1
            elif salida == 2:
                pedido1 = 0
        except ValueError:
            print("Ingrese la opcion correcta") 
    elif Respuesta == 2:
        Otaku_roll= input("Has agregado la opcion Otaku Roll, ¿Cuantos deseas llevar?:\n ")
        total = (Otaku_roll*roll2)
        try:
            salida = int(input("Deseas agregar otra cosa?\n 1=si\n 2=no\n "))
            if salida == 1:
                pedido1 = 1
            elif salida == 0:
                pedido1 = 2
        except ValueError:
            print("Ingrese opcion valida")
    elif Respuesta == 3:
        AnguilaElectrica_roll=input("Has agregado la opcion Anguila Roll, ¿Cuantos deseas llevar?:\n ")
        total = (AnguilaElectrica_roll*roll3)
        try:
            salida=int(input("Deseas agregar otra cosa?\n 1=si\n 2=no\n"))
            if salida == 1:
                pedido1 = 1
            elif salida ==1:
                pedido1 = 2
        except ValueError:
            print("Ingresa una opcion valida")
    elif Respuesta == 4:
        PulpoVenenoso_roll=input("Has agregado la opcion Pulpo Venenoso, ¿Cuantos deseas llevar?\n")
        total = (PulpoVenenoso_roll*roll4)
        try: 
            salida =int(input("Deseas agregar otra cosa?\n 1=si\n 2=no\n"))
            if salida == 1:
                pedido1 = 1
            elif salida ==1:
                pedido1 = 2
        except ValueError:
            print("ingresa opcion valida")
    
    while descuento ==1:
        descuento= input("Ingrese el codigo de descuento") 
        if descuento == "soyotaku":
            descuento = (total/100)*10
            pedido1 = 1
        else:
            print("Has ingresado mal el codigo de descuento")