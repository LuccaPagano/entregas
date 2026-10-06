altura = int(input("Ingrese su altura en cm para determinar su posición: "))

if altura < 160 and altura > 0:
    print("Juega de base")
elif altura <= 179 and altura > 0:
    print("Juega de escolta")
elif altura <= 199 and altura > 0:
    print("Juega de alero")
elif altura <= 200 and altura > 0:
    print("Juega de Ala-Pívot o pívot")
else:
    print("Ingreso mal la altura")
