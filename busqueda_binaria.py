import random


def busqueda_binaria(lista, comienzo, fin, objectivo):
    if comienzo > fin:
        return False
    
    medio = (comienzo + fin) // 2

    if lista[medio] == objectivo:
        return True
    elif lista[medio] < objectivo:
        return busqueda_binaria(lista, medio + 1, fin, objectivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objectivo)

if __name__ == '__main__':
    tamano = int(input('Inserte el tamaño'))
    lista = sorted([random.randint(0, 100) for i in range(tamano)])
    print(lista)
    objectivo = int(input('Cual quiere encontrar'))

    encontrado = busqueda_binaria(lista, 0, len(lista), objectivo)


    print(f'Elemento {objectivo} {"esta" if encontrado else "no esta"} en la lista')
