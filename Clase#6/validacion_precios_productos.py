#POSIBLE SOLUCIÓN - 1

# precio= float(input("Ingrese el precio del producto:"))

# while precio <= 0:
#     precio= float(input("Por favor, ingresa un valor mayor a 0:"))
# print(f"Precio cargado: ${precio}")


#POSIBLE SOLUCIÓN - 2

# precio= -1

# while precio <= 0:
#     try:
#         precio= float(input("Ingrese el precio del producto (debe ser mayor a 0):"))
#         if precio <= 0:
#             print("Error: Por favor, ingresa un valor mayor a 0.")
#     except ValueError:
#         print("Error: Por favor, ingresá un valor numérico válido.")
# print(f"Precio aceptado: ${precio}")


#EJEMPLO PRÁCTICO TRY AND EXCEPT - 1:

# try:
#     precio= float(input("Ingresá el precio del producto:"))
# except ValueError:
#     print("Error: Ingresá un valor numérico válido.")


#EJEMPLO PRÁCTICO TRY AND EXCEPT - 2

while True:
    try:
        num1= float(input("Ingrese el primer número:")) #SOLICITA PRIMER NÚMERO
        num2= float(input("Ingrese el segundo número:")) #SOLICITA SEGUNDO NÚMERO

        resultado= num1 / num2 #INTETO DE DIVIDIR AMBOS NÚMEROS
        print(f"La división de {num1} y {num2} es de: {resultado}") #MOSTRAR EL RESULTADO
        break #SALE DEL BUCLE SI LA DIVISIÓN FUE CORRECTA
    except ZeroDivisionError:
        print("Error: No se puede dividir por 0, por favor vuelva a intentar.") #CONTROLAR LA DIVISIÓN POR 0
    except ValueError: 
        print("Error: Ingresá solamente números que sean válidos.") #MANEJA EL ERROR POR UNA ENTRADA NO VÁLIDA

