import random as rand

def matrices(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = rand.randint(1,10)
            matriz[i].append(num)
    return matriz


def escalar(matriz,n):
    for i in matriz:
        for j in range(len(i)):
            i[j] = n*i[j]
    print(matriz)


            

def app():
    Filas = int(input('Ingrese el número de filas: '))
    Columnas = int(input('Ingrese el número de Columnas: '))
    matriz = matrices(Filas,Columnas)
    print(matriz)
    n = int(input('Ingrese un numero para escalar la matriz: '))
    escalar(matriz,n)


if __name__=="__main__":
    app()