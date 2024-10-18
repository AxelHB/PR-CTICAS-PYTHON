#SOLICITAR AL USUARIO CANTIDAD ACTUAL DE STOCK

cantidad_stock= int(input("Ingrese la cantidad actual de stock del juego:"))

if cantidad_stock <= 1:
    print(f"Tenes en stock {cantidad_stock} juego, REPONER URGENTE")
elif cantidad_stock <= 5:
    print(f"Tenes en stock {cantidad_stock} juegos, RECOMENDABLE REPONER")
else:
    print(f"Tenes en stock {cantidad_stock} juegos, NO HACE FALTA REPONER")