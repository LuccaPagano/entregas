contador_empleados = 0
contador_empleados_masculino = 0
contador_empleados_no_femenino_no_ia = 0
tec_masc_mayor = ""
nombre_masc_mayor = ""
maxima_edad_masc = 0

while contador_empleados < 10:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    while edad < 18:
        print("Usted tiene que ser mayor de edad para ser encuestado.")
        edad = int(input("Ingrese su edad nuevamente: "))
        
    print("Edad correcta.")

    genero = input("Ingrese su género (Masculino, Femenino, Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        print("Ingreso su género incorrectamente.")
        genero = input("Ingrese su género nuevamente (Masculino, Femenino, Otro): ")
        
    print("Ingreso su género correctamente.")

    tec_elegida = input("Elija una tecnología (IA, RV/RA, IOT): ")
    while tec_elegida != "IA" and tec_elegida != "RV/RA" and tec_elegida != "IOT":
        print("Ingreso la tecnología incorrecta. Debe elegir entre (IA, RV/RA, IOT).")
        tec_elegida = input("Elija una tecnología nuevamente (IA, RV/RA, IOT): ")
    print("Tecnología correcta.")

    if genero == "Masculino" and (tec_elegida == "IA" or tec_elegida == "IOT") and edad >= 25 and edad <= 50:
        contador_empleados_masculino += 1


    if genero != "Femenino" and (tec_elegida != "IA") and edad >= 33 and edad <= 40:
        contador_empleados_no_femenino_no_ia += 1

    contador_empleados += 1
    porcentaje = contador_empleados_no_femenino_no_ia / contador_empleados * 100

    if genero == "Masculino" and edad > maxima_edad_masc:
        maxima_edad_masc = edad
        nombre_masc_mayor = nombre
        tec_masc_mayor = tec_elegida

print(f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años es de: {contador_empleados_masculino}")
print(f"Porcentaje de empleados que no son de género femenino y no votaron por IA, cuya edad esté entre 33 y 40 años es de: {porcentaje:.2f}%")
print(f"{nombre_masc_mayor} tiene {maxima_edad_masc} años. Y es el empleado masculino de mayor edad. Eligió {tec_masc_mayor}")
    