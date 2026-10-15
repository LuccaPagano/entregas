apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad (18-90): "))

while edad < 18 or edad > 90:
    print("Edad no permitida. Rango de edad (18-90)")
    edad = int(input("Ingrese nuevametente su edad (18-90): "))
print(f"{apellido} ha ingresado correcta su edad.")

estado_civil = input("Ingrese su estado civil (soltero/a, casado/a, divorciado/a, viudo/a): ")

while estado_civil != "soltero" and estado_civil != "soltera" and estado_civil != "casado" and estado_civil != "casada" and estado_civil != "divorciado" and estado_civil != "divorciada" and estado_civil != "viudo" and estado_civil != "viuda":
    print("Estado civil incorrecto. Debe ser soltero/a, casado/a, divorciado/a, viudo/a.")
    estado_civil = input("Ingrese su estado civil nuevamente (soltero/a, casado/a, divorciado/a, viudo/a): ")
print(f"{apellido} ingreso correcta su estado civil.")


legajo = input("Ingrese su legajo de 4 cifras y sin ceros a la izquierda: ")

while len(legajo) != 4 or legajo[0] == "0":
    print("Legajo incorrecto: debe tener 4 dígitos y no empezar con 0.")
    legajo = input("Ingrese su legajo nuevamente: ")


print(f"{apellido} ingresó correctamente su legajo.")

print("Todos los datos se han ingresado correctamente.")

print(f"""\n
Usted es {apellido}. 
Tiene {edad} años.
Estado civil {estado_civil}.
Número de legajo {legajo}.
""")
