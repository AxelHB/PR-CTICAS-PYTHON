#ARMADO DE FACTURA
factura = int(input("Nro de Factura:"))
mesa = int(input("Nro de Mesa:"))
consumidorFinal = str(input("Nombre del Consumidor Final:"))

print("\n")

#CÁLCULO DE SERVICIO
porcentajePropina = int(input("Ingresá el porcentaje de Propina:")) #PROPINA SUELE RONDAR ENTRE 15% A 20%
total = float(input("Introduzca monto total a pagar:"))
propina = (porcentajePropina/100) * total

print("\n")

#IMPRESIÓN DE FACURA 
print("Restaurante Python\n")
print("Factura N° " , "\t \t" , factura)
print("Mesa N°: " , "\t \t" , mesa)
print("Consumidor Final: " , "\t" , consumidorFinal)

print("\n")

#LISTA DE CONSUMOS
print ("Unidades \t Descripción")
print ("2. \t \t gaseosa")
print ("1. \t Tira de Asado")
print ("1. \t Guarnición")

print("\n")

#TOTAL A PAGAR CON PROPINA
print("El monto total a pagar es de: $" , total , "\n" ,
      "Con la propina del " , porcentajePropina , "%" , " quedaría en: $" , propina , "\n" ,
      "Total a Pagar: " , propina + total)

#EL MONTO TOTAL A PAGAR ES DE $10000
#CON LA PROPINA DEL ...% QUEDARÍA EN $...
#TOTAL A PAGAR = LA SUMA DE LA PROPINA CON EL TOTAL DE CONSUMO