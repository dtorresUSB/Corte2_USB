#-------- Clase Padre --------
class Deportista:
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre= nombre
        self.__documento=documento
        self.__edad=edad

    # ---------- Getters --------------
    def getNombre(self):
        return self.__nombre

    def getDocumento(self):
        return self.__documento
    
    def getEdad(self):
        return self.__edad

    # ------------ Setters -----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setDocumento(self,documento:int):
        self.__documento=documento

    def setEdad(self,edad:int):
        self.__edad=edad

    # ------ Sobrecarga metodo -----
    def palmares(self):
        return 'Gano una medalla'

#-------- Clase Hijo ----------
class DeportistaFutbol(Deportista):
    def __init__(self, nombre: str, documento: \
        int, edad: int,golesAnotados:int,\
            nombreEquipo:str):
        super().__init__(nombre, documento, edad)
        self.__golesAnotados=golesAnotados
        self.__nombreEquipo=nombreEquipo
    
    # ------- Getters Hijo ----------
    def getGolesAnotados(self):
        return self.__golesAnotados

    def getNombreEquipo(self):
        return self.__nombreEquipo

    # -------- Setters Hijo ----------
    def setGolesAnotados(self,golesAnotados:int):
        self.__golesAnotados=golesAnotados
    
    def setNombreEquipo(self,nombreEquipo:str):
        self.__nombreEquipo=nombreEquipo

    # ------ Sobrecarga metodo -----
    def palmares(self):
        return 'Gano la Europa UEFA League'

def main():
    Futbolista = DeportistaFutbol('Falcao',24152637,36,\
        35,'Selección Colombia')
    
    print(f'Deportista: {Futbolista.getNombre()}\n'+\
    f'Documento:{Futbolista.getDocumento()}\n'+\
    f'Edad:{Futbolista.getEdad()}\n'+\
    f'Cantidad de Goles:{Futbolista.getGolesAnotados()}\n'+\
    f'Equipo:{Futbolista.getNombreEquipo()}\n'+\
        f'Palmares:{Futbolista.palmares()}\n')
    
    futbolista2=Deportista('Mario Yepes',626353,48)
    print(f'Deportista: {futbolista2.getNombre()}\n'+\
    f'Documento:{futbolista2.getDocumento()}\n'+\
    f'Edad:{futbolista2.getEdad()}\n'+\
        f'Palmares:{futbolista2.palmares()}')

if __name__ == "__main__":
    main()