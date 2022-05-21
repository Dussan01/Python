import random


def busqueda_lienal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tamano_lista = int(input('tamano de la lista?'))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    #lista = []
    #for i in range(tamano_lista):
    #    lista = random.randint(0,100)

    print(lista)
    objectivo = int(input('Que numero quiere encontrar?'))

    encontrado = busqueda_lienal(lista, objectivo)
    print(f'Elemento {objectivo} {"esta" if encontrado else "no esta"} en la lista')