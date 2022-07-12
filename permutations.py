import random


def main():
    contador = 1
    me = input("Ingresa tu nombre: ")
    succs = [me]
    me = nombre(me)
    print(me)
    permutaciones = factorial(len(me))

    while contador != permutaciones:
        random.shuffle(me)
        suc = ""

        for elem in me:
            suc = "".join([suc, str(elem)])

        if suc not in succs:
            succs.append(suc)
            print(suc)
            contador += 1
            continue

        else:
            continue

    print(f"Se encontraron: {contador} permutaciones")


def factorial(numero):
    valor = numero
    numeros = []
    factorial = 1

    for numero in range(1, valor + 1, 1):
        numeros.append(numero)
    numeros = numeros[::-1]

    for numero in numeros:
        factorial *= numero
    return factorial


def nombre(string):
    string = list(string)
    return string


main()