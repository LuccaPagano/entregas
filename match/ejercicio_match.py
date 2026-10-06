estacion_anio = input("Ingrese la estación del año: ")

match estacion_anio:
    case "invierno":
        print("Solo se viaja a Bariloche")

    case "verano":
        print("Solo se viaja a Mar del Plata y Cataratas")

    case "otoño":
        print("Se puede viajar a cualquier lugar")

    case "primavera":
        print("Se viaja a todos los lugares menos Bariloche.")

    case _:
        print("No se viaja")

