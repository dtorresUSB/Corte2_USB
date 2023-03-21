
milista =[3,5,7]
while 1:
    opc = input('Ingrese un dato: ')
    if opc == 'borrar':
        milista.clear()
    else:
        idx = int(input('Ingrese un indice: '))
        milista.insert(idx,opc)
        print(milista)
