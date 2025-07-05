def convertir_fecha(fecha_input):

    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    fecha_input = fecha_input.strip()

    try:
        if "/" in fecha_input:
            partes = fecha_input.split("/")
            mes = int(partes[0])
            dia = int(partes[1])
            anio = int(partes[2])
        else:
            partes = fecha_input.replace(",", "").split()
            mes_nombre = partes[0].capitalize()
            if mes_nombre in meses:
                mes = meses.index(mes_nombre) + 1
            else:
                print("Mes no válido.")
                return
            dia = int(partes[1])
            anio = int(partes[2])

        print(f"{anio}-{mes:02d}-{dia:02d}")

    except:
        print("Formato de fecha inválido. Intente con 'MM/DD/AAAA' o 'Mes DD, AAAA'.")

entrada = input("Ingrese una fecha (MM/DD/AAAA o Mes DD, AAAA): ")
convertir_fecha(entrada)