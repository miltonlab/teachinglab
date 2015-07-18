def buscar(arreglo, buscado):
    r = binaria_recursiva(arreglo, buscado, 0, len(arreglo)-1)
    if r > 0:
        print('elemento ', buscado, 'encontrado en: ', r)
    else:
        print ('elemento ', buscado, 'NO encontrado')

def binaria_recursiva(arreglo, buscado, izq, der):
    centro = (izq + der) // 2
    print(arreglo[izq:der+1])
    if buscado == arreglo[centro]:
        return centro
    elif buscado < arreglo[centro]:
        return binaria_recursiva(arreglo, buscado, izq, centro-1)
    else:
        return binaria_recursiva(arreglo, buscado, centro+1, der)
    return -1

if __name__ == '__main__':
    # a = [1,2,3,4,5,6,7,8,9]
    # buscar(a, 9)
    a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    buscar(a, 19)