import os
import time
limpieza_pantalla = "cls"

#Definicion de variables

Pickachu_roll = 4500
Otaku_roll = 5000
PulpoVenenoso_roll = 5200
AnguilaElectrica_roll = 4800
total = 0
descuentoSoyOtaku = 0 
Respuesta = 0
i= True

print("Bienvenido a Sushi Otaku Delivery")
print("A continuacion le mostrare el menu que tenemos disponible")
print("1. Pickachu Roll: $4.500.-\n 2. Otaku Roll: $5.000.-\n 3. Pulpo Venenoso Roll: $5.200.-\n 4. Anguila Electrica: $4.800.-")
print("Por favor seleccione las opciones que desea agregar")

while True:
    Respuesta= int(input("Has selesccionado la opcion 1: {pickachu_roll}"))
    if Respuesta == 1:
        input("Has pedido Pickachu Roll")
    elif Respuesta == 2:
        Respuesta = int(input("Has seleccionado la opcion 2: {otaku_roll}"))
    elif Respuesta == 3:
        Respuesta = int(input("Has seleccionado la opcion 3: {PulpoVenenoso_roll}"))
    elif Respuesta == 4:
        Respuesta = int(input("Has seleccionado la opcion 4: {AnguilaElectrica_roll}"))
    else:
        Respuesta = input("No has seleccionado ninguna opcion")
        break




