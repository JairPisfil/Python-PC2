numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().lower()
    
    if respuesta == "no":
        break
    if respuesta == "si":
        numero = input("Ingrese el número: ")
        if numero.isdigit():
            numeros.append(int(numero))
        else:
            print("Por favor, ingrese un número válido.")
    else:
        print("Respuesta no válida. Escriba 'SI' o 'NO'.")

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)