# print("1. Números ascendentes:")
# numero = 1
# while numero <= 10:
# 	print(numero)
# 	numero += 1

# print("\n2. Números descendentes:")
# numero = 10
# while numero >= 1:
# 	print(numero)
# 	numero -= 1

# print("\n3. Suma del 1 al 10:")
# numero = 1
# suma = 0
# while numero <= 10:
# 	suma += numero
# 	numero += 1
# print(suma)

# print("\n4. Suma de los números pares del 1 al 10:")
# numero = 1
# suma_pares = 0
# while numero <= 10:
# 	if numero % 2 == 0:
# 		suma_pares += numero
# 	numero += 1
# print(suma_pares)

# print("\n5. Ingrese 5 números:")
# contador = 0
# suma = 0
# while contador < 5:
# 	suma += float(input(f"Número {contador + 1}: "))
# 	contador += 1
# print(f"Suma: {suma}")
# print(f"Promedio: {suma / 5}")

# print("\n6. Ingrese números. Escriba 'fin' para terminar.")
# suma = 0
# contador = 0
# while True:
# 	entrada = input("Número: ")
# 	if entrada.lower() == "fin":
# 		break
# 	suma += float(entrada)
# 	contador += 1
# if contador > 0:
# 	print(f"Suma: {suma}")
# 	print(f"Promedio: {suma / contador}")
# else:
# 	print("No se ingresaron números.")

# print("\n7. Ingrese números. Escriba 'fin' para terminar.")
# suma_positivos = 0
# producto_negativos = 1
# hay_negativos = False
# while True:
# 	entrada = input("Número: ")
# 	if entrada.lower() == "fin":
# 		break
# 	numero = float(entrada)
# 	if numero > 0:
# 		suma_positivos += numero
# 	elif numero < 0:
# 		producto_negativos *= numero
# 		hay_negativos = True
# print(f"Suma de positivos: {suma_positivos}")
# if hay_negativos:
# 	print(f"Producto de negativos: {producto_negativos}")
# else:
# 	print("No se ingresaron números negativos.")

print("\n8. Ingrese 10 números enteros:")
contador = 0
flag_maximo = False
flag_minimo = False
maximo = 0
minimo = 0
while contador < 10:
	numero = int(input(f"Número {contador + 1}: "))
	if flag_maximo == False or numero > maximo:
		maximo = numero
		flag_maximo = True
		
	if flag_minimo == False or numero < minimo:
		minimo = numero
		flag_minimo = True
	contador += 1
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# print("\n9. Ingrese 5 numeros:")
# contador = 0
# suma = 0
# while contador < 5:
# 	numero = float(input(f"Número {contador + 1}: "))
# 	suma += numero
# 	contador += 1
# print(f"Suma: {suma}")
# print(f"Promedio: {suma / 5}")

# print("\n10. Ingrese 5 numeros como mínimo y 10 como máximo:")
# contador = 0
# suma = 0
# while contador < 10:
# 	numero = float(input(f"Número {contador + 1}: "))
# 	suma += numero
# 	contador += 1
# 	if contador >= 5:
# 		continuar = input("¿Desea ingresar otro número? (s/n): ")
# 		if continuar != "s":
# 			break
# print(f"Suma: {suma}")
# print(f"Promedio: {suma / contador:.2f}")

# INTEGRADOR

