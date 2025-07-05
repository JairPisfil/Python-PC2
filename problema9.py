def eliminar_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for letra in texto:
        if letra not in vocales:
            resultado += letra
    return resultado

entrada = input("Ingrese un texto: ")
salida = eliminar_vocales(entrada)
print("Texto sin vocales:", salida)