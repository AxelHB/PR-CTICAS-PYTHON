#PETICIÓN DE NOMBRE, CANTIDAD Y VALOR UNITARIO DE PRODUCTOS

#ENTRADA:
#Solicitud: datos Primer Producto.
producto1= input("Ingrese el nombre del primer producto:")
cantidad1= int(input (f"Ingrese la cantidad del producto {producto1}: ")) 
valor_unitario_1= float(input(f"Ingrese el valor unitario del producto {producto1}:"))

#Solicitud: datos Segundo Producto.
# producto2= input("Ingrese el nombre del segundo producto:")
# cantidad2= int(input (f"Ingrese la cantidad del producto {producto2}: ")) 
# valor_unitario_2= float(input(f"Ingrese el valor unitario del producto {producto2}:"))

#Solicitud: datos Tercer Producto.
# producto3= input("Ingrese el nombre del tercer producto:")
# cantidad3= int(input (f"Ingrese la cantidad del producto {producto3}: ")) 
# valor_unitario_3= float(input(f"Ingrese el valor unitario del producto {producto3}:"))

#PROCESO:
#CÁLCULO DE TOTALES
#PRODUCTO#1
total1= cantidad1 * valor_unitario_1
iva1= total1 * 0.21
total_con_iva1= iva1 + total1

#PRODUCTO#2
# total2= cantidad2 * valor_unitario_2
# iva2= total2 * 0.21
# total_con_iva2= iva2 + total2

#PRODUCTO#3
# total3= cantidad3 * valor_unitario_3
# iva3= total3 * 0.21
# total_con_iva3= iva3 + total3

#SALIDA:
print("\n --- TICKET DE COMPRA --- \n")
print("--- PRODUCTO #1 ---")
print(f"Producto: {producto1}")
print(f"Cantidad: {cantidad1}")
print(f"Valor Unitario: ${valor_unitario_1}")
print(f"Total sin IVA: ${total1}")
print(f"IVA (%21): ${iva1:.2f}")
print(f"Total de Compra con el IVA: ${total_con_iva1:.2f}")

# print("--- PRODUCTO #2 ---")
# print(f"Producto: {producto2}")
# print(f"Cantidad: {cantidad2}")
# print(f"Valor Unitario: ${valor_unitario_2}")
# print(f"Total sin IVA: ${total2}")
# print(f"IVA (%21): ${iva2:.2f}")
# print(f"Total de Compra con el IVA: ${total_con_iva2:.2f}")

# print("--- PRODUCTO #3 ---")
# print(f"Producto: {producto3}")
# print(f"Cantidad: {cantidad3}")
# print(f"Valor Unitario: ${valor_unitario_3}")
# print(f"Total sin IVA: ${total3}")
# print(f"IVA (%21): ${iva3:.2f}")
# print(f"Total de Compra con el IVA: ${total_con_iva3:.2f}")
