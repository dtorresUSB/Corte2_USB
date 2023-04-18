
class Ciudadano():
    def __init__(self):
        self.__nombre=None
        self.__idioma=None
    
    # ----- Getters -------
    def getNombre(self):
        return self.__nombre
    
    def getIdioma(self):
        return self.__idioma
    
    #------- Setters --------
    def setNombre(self,nombre:str):
        self.__nombre = nombre

    def setIdioma(self,idioma:str):
        self.__idioma=idioma

    # ------- Sobrecarga --------
    def saludo(self):
        return "Quoi de beau!"
    
class Colombia(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__cc=None
    
    def setCC(self,cc:int):
        self.__cc=cc

    def getCC(self):
        return self.__cc
    
    # ------- Sobrecarga --------
    def saludo(self):
        return "Qiubo Parce!!"

class Inglaterra(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__id=None
    
    def setId(self,id:int):
        self.__id=id

    def getId(self):
        return self.__id
    
    # ------- Sobrecarga --------
    def saludo(self):
        return "Hello my friend!"

class China(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__shengfenzheng=None
    
    def setShengfenzheng(self,shengfenzheng:int):
        self.__shengfenzheng=shengfenzheng

    def getShengfenzheng(self):
        return self.__shengfenzheng
    
    # ------- Sobrecarga --------
    def saludo(self):
        return "你干嘛呀！!"

def darSaludo(obj):
    return obj.saludo()
    

def main():
    colombiano = Colombia()
    colombiano.setNombre('Kevin')
    colombiano.setIdioma('Español')
    colombiano.setCC(1524348)

    ingles = Inglaterra()
    ingles.setNombre('Richard')
    ingles.setIdioma('English')
    ingles.setId(3937593)

    chino = China()
    chino.setNombre('Liu')
    chino.setIdioma('汉语')
    chino.setShengfenzheng(626525362)

    Ciudadano1 = Ciudadano()
    Ciudadano1.setNombre('Carla')
    Ciudadano1.setIdioma('Frances')

    #----- Aplicantes -----
    print(f'Aplicante: {colombiano.getNombre()}\n'+\
        f'Idioma: {colombiano.getIdioma()}\n' + \
            f'CC: {colombiano.getCC()}\n'+
            darSaludo(colombiano)+'\n')
    
    print(f'Aplicante: {ingles.getNombre()}\n'+\
        f'Idioma: {ingles.getIdioma()}\n' + \
            f'Id: {ingles.getId()}\n'+
            darSaludo(ingles)+'\n')

    print(f'Aplicante: {chino.getNombre()}\n'+\
        f'Idioma: {chino.getIdioma()}\n' + \
            f'省份证: {chino.getShengfenzheng()}\n'+
            darSaludo(chino)+'\n')

    print(f'Aplicante: {Ciudadano1.getNombre()}\n' + \
        f'Idioma: {Ciudadano1.getIdioma()}\n'+\
            darSaludo(Ciudadano1))

    

if __name__=="__main__":
    main()