def contar_digito(numero, digito):

    numero_str = str(numero)
    digito_str = str(digito)
    
    cantidad = numero_str.count(digito_str)
    
    print(f"Cantidad de veces {digito} en el número {numero}: {cantidad}")
    return cantidad

contar_digito(15789000, 0)