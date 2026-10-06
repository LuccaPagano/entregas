cargo_fijo = 7000
costo_m_cubico = 200

while True:
    tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial o Industrial): ").upper()
    if tipo_cliente == "RESIDENCIAL" or tipo_cliente == "COMERCIAL" or tipo_cliente == "INDUSTRIAL":
        
        consumo = float(input("Ingrese el consumo de agua en metros cúbicos: "))
        


        match tipo_cliente:
            
                case "RESIDENCIAL":
                    costo_consumo = consumo * costo_m_cubico
                    bonificacion = 0
                    recargo = 0
                    
                    if consumo < 30 and consumo > 0:
                        bonificacion = costo_consumo * 0.10
                    elif consumo > 80:
                        recargo = costo_consumo * 0.15
                    elif consumo >= 30 and consumo <= 80:
                        print(f"Usted ha consumido {consumo} metros cúbicos, no se aplicará bonificación ni recargo.")
                    else:
                        print("Usted no ha consumido nada, por lo tanto solo se le cobrará el cargo fijo.")


                    subtotal_consumo = cargo_fijo + costo_consumo
                    sub_total = subtotal_consumo + recargo

                    if sub_total < 35000 and consumo > 0:
                        bonificacion += sub_total * 0.05
                        print("El total de la factura sin impuestos ni bonificaciones es menor a $35000, por lo tanto se le aplicará una bonificación adicional del 5%")

                    total_pagar = sub_total - bonificacion

                    iva = total_pagar * 0.21
                    total_con_iva = total_pagar + iva

                    print("Resumen de la factura:")

                    print(f"Consumo: {consumo} metros cúbicos")
                    print(f"Costo por consumo: ${costo_consumo:.2f}")
                    print(f"Bonificación: ${bonificacion:.2f}")
                    print(f"Recargo: ${recargo:.2f}")
                    print(f"Total sin IVA: ${total_pagar:.2f}")
                    print(f"IVA (21%): ${iva:.2f}")
                    print(f"Total a pagar: ${total_con_iva:.2f}")

                case "COMERCIAL":
                    costo_consumo = consumo * costo_m_cubico
                    bonificacion = 0
                    recargo = 0

                    if consumo > 0 and consumo < 50:
                        recargo = costo_consumo * 0.05
                        print(f"Usted ha consumido {consumo} metros cúbicos, se aplicará un recargo del 5%")
                    elif consumo >= 50 and consumo <= 150:
                        print(f"Usted ha consumido {consumo} metros cúbicos, no se aplicará bonificación ni recargo.")

                    elif consumo > 150 and consumo <= 300:
                        bonificacion = costo_consumo * 0.08
                        print(f"Usted ha consumido {consumo} metros cúbicos, se aplicará una bonificación del 8%")

                    elif consumo > 300:
                        bonificacion = costo_consumo * 0.12
                        print(f"Usted ha consumido {consumo} metros cúbicos, se aplicará una bonificación del 12%")
                        
                    else:
                        print(f"Usted no ha consumido nada, por lo tanto solo se le cobrará el cargo fijo.")

                    subtotal_consumo = cargo_fijo + costo_consumo
                    total_pagar = subtotal_consumo - bonificacion + recargo
                    iva = total_pagar * 0.21
                    total_con_iva = total_pagar + iva

                    print("Resumen de la factura:")

                    print(f"Consumo: {consumo} metros cúbicos")
                    print(f"Bonificación: ${bonificacion:.2f}")
                    print(f"Costo por consumo: ${costo_consumo:.2f}")
                    print(f"Total sin IVA: ${total_pagar:.2f}")
                    print(f"IVA (21%): ${iva:.2f}")
                    print(f"Total a pagar: ${total_con_iva:.2f}")

                case "INDUSTRIAL":
                    costo_consumo = consumo * costo_m_cubico
                    bonificacion = 0
                    recargo = 0

                    if consumo > 0 and consumo < 200:
                        recargo = costo_consumo * 0.10
                        print(f"Usted ha consumido {consumo} metros cúbicos, se aplicará un recargo del 10%")

                    elif consumo > 500 and consumo < 1000:

                        bonificacion = costo_consumo * 0.20
                        print(f"Usted ha consumido {consumo} metros cúbicos, se aplicará una bonificación del 20%")

                    elif consumo > 1000:
                        bonificacion = costo_consumo * 0.30
                        print(f"Usted ha consumido {consumo} metros cúbicos, se aplicará una bonificación del 30%")

                    else:
                        print(f"Usted no ha consumido nada, por lo tanto solo se le cobrará el cargo fijo.")



                    subtotal_consumo = cargo_fijo + costo_consumo
                    total_pagar = subtotal_consumo - bonificacion + recargo
                    iva = total_pagar * 0.21
                    total_con_iva = total_pagar + iva

                    print("Resumen de la factura:")

                    print(f"Consumo: {consumo} metros cúbicos")
                    print(f"Costo por consumo: ${costo_consumo:.2f}")
                    print(f"Bonificación: ${bonificacion:.2f}")
                    print(f"Recargo: ${recargo:.2f}")
                    print(f"Total sin IVA: ${total_pagar:.2f}")
                    print(f"IVA (21%): ${iva:.2f}")
                    print(f"Total a pagar: ${total_con_iva:.2f}")


        continuar = input("¿Desea realizar otra facturación? (SI/NO): ").upper()

        if continuar == "NO":
            print("Gracias por usar el sistema de facturación.")
            break
    else:
        print("Tipo de cliente no válido.") 