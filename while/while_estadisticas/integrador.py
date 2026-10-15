continuar = "s"
contador = 0
suma_positivos = 0
suma_negativos = 0
contador_positivos = 0
contador_negativos = 0
bandera_positivos = False
max_cant_positivos = 0

while continuar == "s":
	numero = int(input("Ingrese un número: "))
	print(f"Número {contador + 1}: {numero}")
	contador += 1
	if numero > 0:
		suma_positivos += numero
		contador_positivos += 1
		
		if bandera_positivos == False or numero > max_cant_positivos:
			bandera_positivos = True
			max_cant_positivos = numero
	
	elif numero < 0:
		suma_negativos += numero
		contador_negativos = contador_negativos + 1

	else:
		print("No ha ingresado ningún número")

	continuar = input("¿Desea ingresar otro número? (s/n): ")


print(f"Suma de negativos: {suma_negativos}")
print(f"Suma de positivos: {suma_positivos}")
print(f"Cantidad de números negativos ingresados {contador_negativos}")

if contador_positivos > 0:
	print(f"Promedio de positivos: {suma_positivos / contador_positivos}")

print(f"El número positivo más grande ingresado es: {max_cant_positivos}")

if contador > 0:
    porcentaje_negativos = contador_negativos / contador * 100
    print(f"Porcentaje de números negativos, respecto al total de números ingresados es de: {porcentaje_negativos}%")


