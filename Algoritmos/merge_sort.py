import random

lista_ordenada = []

def unir_listas(lista_1, lista_2):
    #Esta función asume que las listas estan ordenadas
    nueva_lista = []

    #Se ejecuta el while miestras ambas listas estén NO vacías
    while len(lista_1) > 0 and len(lista_2) > 0:
        if lista_1[0] <= lista_2[0]:
            nueva_lista.append(lista_1.pop(0))
        else:
            nueva_lista.append(lista_2.pop(0))

    #Al quedar una lista vacía agregamos el resto de la otra lista
    nueva_lista.extend([item for item in lista_1 if len(lista_2) == 0])
    nueva_lista.extend([item for item in lista_2 if len(lista_1) == 0])
    
    return nueva_lista


def merge_sort(lista, inicio, final):
    if final - inicio < 2:
        return sorted(lista[inicio:final+1].copy())
    
    punto_medio = (final + inicio) // 2
    izquierda = merge_sort(lista, inicio, punto_medio)
    derecha = merge_sort(lista, punto_medio + 1, final)

    #print(f'izquierda {izquierda} derecha {derecha}')

    lista_ordenada.extend(unir_listas(izquierda, derecha))

    return lista_ordenada



if __name__ == '__main__':
    n = 5    #tamaño y rango de la lista ejemplo
    lista = [random.randint(0, n) for item in range(0, n)]
    print(lista)

    nueva = merge_sort(lista, 0, n - 1)
    print(nueva)

    #izquierda, derecha, punto_medio = merge_sort(lista, 0, n - 1) #La función debe recibir los índices extremos de la lista

    