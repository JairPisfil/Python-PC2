def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingrese un número: "))
if es_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} No es un número primo.")