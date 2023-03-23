def impar(x):
    if x <=0:
        return 0
    else:
        num = (2*x-1) + impar(x-1)
        return num

def app():
    n = int(input('Cuantos numeros desea generar: '))
    for i in range(n):
        valor = impar(i)
        print(valor, end= ' ')

if __name__ == "__main__":
    app()
