milista =[3,5,7,5]
opc =''
while opc != 'salir':
    opc = input('¿Que metodo desea utilizar? ')
    if opc == 'agregar':
        dato = int(input('¿Cual dato quiere agregar? '))
        milista.append(dato)
        print(milista)
    
    elif opc == 'limpiar':
        milista.clear()
        print(milista)
    
    elif opc == 'borrar':
        dato = int(input('¿Cual dato quiere borrar? '))
        milista.remove(dato)
        print(milista)

    elif opc == 'buscar':
        dato = int(input('¿Cual dato quiere buscar? '))
        pos = milista.index(dato)
        print(f'el indice es {pos}')
        
    elif opc == 'insertar':
        dato =int(input('¿Cual dato quiere insertar? '))
        idx = int(input('Ingrese un indice: '))
        milista.insert(idx,dato)
        print(milista)

    elif opc == 'sacar':
        idx = int(input('Indice del numero a sacar: '))
        milista.pop(idx)
        print(milista)
        
    elif opc == 'comparar':
        print(f'El valor maximo  de la lista es: {max(milista)}')
        print(f'El valor minimo de la lista es: {min(milista)}')
    
    elif opc == 'contar':
        dato = int(input('¿Que numero desea revisar '))
        con = milista.count(dato)
        print(f'el numero {dato} esta {con} veces en la lista')

    elif opc == 'sumar':
        print(f'los elementos de la lista suman {sum(milista)}')

    elif opc == 'comprobar':
        dato = int(input('¿Que dato desea comprobar? '))
        print(dato in milista)
    
    elif opc == 'extender':
        OtraLista = [1,2,3,4]
        milista.extend(OtraLista)
        print(milista)

    elif opc == 'ascender':
        milista.sort()
        print(milista)
    
    elif opc == 'invertir':
        milista.sort(reverse=True)
        print(milista)