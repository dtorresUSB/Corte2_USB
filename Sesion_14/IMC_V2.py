class Personas:
    def __init__(self):
        self.__nombre = None
        self.__altura = None
        self.__peso = None

    # ----------- Getters -------------
    def getNombre(self):
        return self.__nombre

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    # ----------- Setters -------------
    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setAltura(self, altura: int):
        if altura < 40:
            print('Valor de altura erroneo')
        else:
            self.__altura = altura

    def setPeso(self, peso: float):
        if peso < 10:
            print('Valor de peso erroneo')
        else:
            self.__peso = peso

    # ----------- Método IMC privado -------------    
    def __Indice(self):
        IMC=self.__peso/((self.__altura/100)**2)
        if IMC <= 18.5:
            return str('Por debajo')
        elif IMC <=24.9:
            return str('Saludable')
        elif IMC <=29.9:
            return str('Sobrepeso')
        elif IMC <=34.9:
            return str('Obesidad I')
        elif IMC <=39.9:
            return str('Obesidad II')
        else:
            return str('obesidad III')

    # ----------- Invocación Metodo IMC ----------
    def getIMC(self):
        if self.__peso == None or self.__altura == None:
            return('')
        else:
            return self.__Indice()


def main():
    Titulo =['Nombre','Peso','Altura']
    entrada = []
    for i in range(3):
        entrada.append(input(f'Ingrese el {Titulo[i]}: '))

    estudiante = Personas()
    estudiante.setNombre(entrada[0])
    estudiante.setPeso(int(entrada[1]))
    estudiante.setAltura(float(entrada[2]))
    print(f'su IMC es: {estudiante.getIMC()}')


if __name__ == "__main__":
    main()
