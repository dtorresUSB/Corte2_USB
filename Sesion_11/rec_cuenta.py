def imprimir(x):
    if x>0:
        imprimir(x-1)
        print(x)
    else:
        print(f'finalizo {x}')

if __name__ == "__main__":
    imprimir(5)