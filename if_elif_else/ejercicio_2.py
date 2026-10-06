nota = int(input("Ingrese su nota: "))

if nota <= 6 or nota >= 10:
    print(f"Promoción directa, la nota es: {nota}")
elif nota >= 4 or nota <= 5:
    print(f"Aprobado, la nota es: {nota}") 
elif nota <= 4:
    print(f"Reprobado, la nota es: {nota}")
