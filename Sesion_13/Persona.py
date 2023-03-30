
class Persona:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.frase=None
    
    def hablar(self):
        return self.frase
        

def main():
    estudiante = Persona()
    estudiante.nombre = 'Juan'
    estudiante.apellido = 'Mancera'
    estudiante.edad = 19
    estudiante.frase='Oh debo estudiar!'

    futbolista = Persona()
    futbolista.nombre='Radamel'
    futbolista.apellido='García'
    futbolista.edad=36
    futbolista.frase='Gooooooool!'

    print(f'El estudiante dice: {estudiante.hablar()}')
    print(f'El Señor Futbolista dice: {futbolista.hablar()}')

if __name__== '__main__':
    main()