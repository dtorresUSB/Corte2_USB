Estudiantes={'Mancera':{'Edad':19,'Documento':12763729,'Genero':'M'},\
    'Felipe':{'Edad':20,'Documento':12767364,'Genero':'M'},\
        'Jose':{'Edad':18,'Documento':1254532,'Genero':'M'}}
nombres = {1:'Mancera',2:'Felipe',3:'Jose'}

busqueda = int(input('Ingrese un codigo estudiantil: '))
persona = nombres[busqueda]
print(f'La edad de {nombres[busqueda]} es {Estudiantes[persona]["Edad"]}')