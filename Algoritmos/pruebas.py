

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
    
    
        

if __name__ == '__main__':
    listita = unir_listas([1,3,4], [2,4,5])
    print(listita)