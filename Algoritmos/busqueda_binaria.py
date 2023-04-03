import random

def busqueda_binaria(lista, elemento, inicio, final):

    while final - inicio > 1:
        indice_intermedio = (final + inicio) // 2

        if lista[indice_intermedio] == elemento:
            return True
        elif elemento < lista[indice_intermedio]:
            final = indice_intermedio
            continue
        else:
            inicio = indice_intermedio
            continue

    return False



if __name__ == '__main__':
    n = 1000    #tamaño y rango de la lista ejemplo
    lista = sorted([int(n * random.random()) for item in range(0, n)])

    elemento = int(input('Que numero quieres buscar en la lista? '))
    print(f'{"Se encontro" if busqueda_binaria(lista, elemento, 0, len(lista)) else "No se encontro"} el valor {elemento} en la lista')