print("Ejercicio 1")

clave_correcta = "1234"
clave_usuario = input("Ingrese una clave: ")

while clave_usuario != clave_correcta:
    print("Clave incorrecta. Intente nuevamente.")
    clave_usuario = input("Ingrese la clave: ")
print("Clave correcta.")
print("=" * 50)

print("Ejercicio 2")

clave_correcta = "1234"

clave_usuario = input("Ingrese una clave, tiene 3 intentos: ")

intentos = 0

while clave_usuario != clave_correcta and intentos < 2:
    print("Clave incorrecta. Intente nuevamente.")
    clave_usuario = input("Ingrese la clave: ")
    intentos += 1

if clave_usuario == clave_correcta:
    print("Clave correcta.")
else:
    print("Se han agotado los intentos.")
print("=" * 50)

print("Ejercicio 3")

nota = int(input("Ingrese una nota del 1 al 10: "))

while nota < 1 or nota > 10:
    print("Nota incorrecta. La nota debe ser entre 1 y 10")
    nota = int(input("Ingrese una nota del 1 al 10: "))

print("Ha ingresado correctamente su nota")
print("=" * 50)

print("Ejercicio 4")

color = input("Ingrese un color (verde - azul - rojo): ")

while color != "verde" and color != "azul" and color != "rojo":
    print(f"Usted ha ingresado {color}. Color no disponible")
    color = input("Ingrese un color (verde - azul - rojo): ")
print("Ha ingresado correctamente su color")
print("=" * 50)

