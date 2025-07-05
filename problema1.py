resultados = []

for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        resultados.append(numero)

print("Numeros divisibles por 7 y multiplos de 5 entre 1500 y 2700:")
print(resultados)