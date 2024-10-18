#ENTRADA / INPUT
monto_total= float(input("Ingrese el monto total de la compra:"))

cantidad_articulos= int(input("Ingrese la cantidad de artículos:"))

descuento= 0

#PROCESO
if cantidad_articulos >= 5 and monto_total > 10000:
    descuento= (monto_total * 15) / 100
    print(f"Tenés un 15 aplicado a tu compra, descontamos: {descuento}")
elif cantidad_articulos >= 3 and cantidad_articulos < 5:
    descuento= (monto_total * 10) / 100
    print(f"Tenés un 10 aplicado a tu compra, descontamos: {descuento}")
else:
    print("no aplica descuento / promoción")

#SALIDA / OUTPUT
print("\t---TICKET DE COMPRA---\n")
print(f"La compra total fue de: {monto_total - descuento}")