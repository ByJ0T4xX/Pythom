while True:
    print("Bienvenidos a la aplicacion de gestion de sueldos:")
    print("1. Registrar trabajador")
    print("2. Lista todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    opcMenu=int(input("Seleccione una opcion:"))

    if opcMenu==1:
        Nombre = input("Ingrese nombre y apellido del trabajador: ")
        Cargo = input("Ingrese el cargo del trabajador: ")
        Sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
        Desc_salud = Sueldo_bruto * 0.07
        Desc_afp = Sueldo_bruto * 0.12
        Liquido_pagar = Sueldo_bruto - Desc_salud - Desc_afp

        print("Trabajador registrado:")
        print("Nombre y apellido:", Nombre)
        print("Cargo:", Cargo)
        print("Sueldo bruto:", Sueldo_bruto)
        print("Descuento salud:", Desc_salud)
        print("Descuento AFP:", Desc_afp)
        print("Liquido a pagar:", Liquido_pagar)
                #Crear nuevos usuarios en la lista personal.txt
                #return Registro_datos
    elif opcMenu==2:
        with open('Personal.txt',"w") as Archivo:
            Contenido= Archivo.read()
        print("Lista de trabajadores:")
        for trabajador in Contenido:
            print(trabajador)

    elif opcMenu==3:
        if cargo:
            filename = f"planilla_{cargo}.txt"
            with open(filename, "w") as file:
                for trabajador in trabajadores:
            if trabajador[1] == cargo:
                file.write("Nombre y apellido: {}\n" .format(trabajador[0]))
                file.write("Cargo: {}\n" .format(trabajador[1]))
                file.write("Sueldo bruto: {}\n" .format(trabajador[2]))
                file.write("Descuento salud: {}\n" .format(trabajador[3]))
                file.write("Descuento AFP: {}\n" .format(trabajador[4]))

        else:
            filename = "Planilla_todos.txt"
            with open(filename, "w") as file:
                for trabajador in trabajadores:
                    file.write("Nombre y apellido: {}\n".format(trabajador[0]))
                    file.write("Cargo: {}\n".format(trabajador[1]))
                    file.write("Sueldo bruto: {}\n".format(trabajador[2]))
                    file.write("Descuento salud: {}\n".format(trabajador[3]))
                    file.write("Descuento AFP: {}\n".format(trabajador[4]))
                    file.write("Liquido a pagar:{}\n\n".format(trabajador[5]))
    else :
        print("Hasta pronto")
        break