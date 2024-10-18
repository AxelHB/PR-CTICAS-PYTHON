productos= 0
stock_total= 0

while productos != "salir":
    productos= str(input("Ingrese el nombre del Producto (o escribí 'salir' para terminar):"))

    if productos.lower() != "salir":
        cantidad= int(input("Ingrese la cantidad en stock:")) 
        stock_total += cantidad #ACUMULAMOS EL TOTAL DE PRODUCTOS INGRESADOS
else: #NO ES INDISPENSABLE SU USO, YA QUE WHILE NO REQUIERE DE UN ELSE. Y EL IF ES INDEPENDIENTE
        print(f"El stock total es de {stock_total}")

