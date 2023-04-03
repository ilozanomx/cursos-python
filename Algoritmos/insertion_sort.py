import random

def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1
        while j > -1:   #recorre los indices i-1 -> 0
            if lista[j] > valor_actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                lista[j + 1] = valor_actual
                break
        if j == -1: #será True solo si valor_actual es menor que todos los valores en el rango i-1 -> 0
            lista[0] = valor_actual
    
    return lista


if __name__ == '__main__':
    n = 11    #tamaño y rango de la lista ejemplo
    lista = [random.randint(0, n) for item in range(0, n)]

    print(lista)
    lista = insertion_sort(lista)

    print(lista)