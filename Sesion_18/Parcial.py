

class Articulos():
    def __init__(self):
        self.__idArticulo=None
        self.__precioBase=None
        self.__unidExistencia=None

    def setidArticulo(self,id:int):
        self.__idArticulo=id
    
    def setPrecioBase(self,precio:float):
        self.__precioBase=precio
    
    def setUnidExistente(self,unidad:int):
        self.__unidExistencia=unidad

    def getIdArticulo(self):
        return self.__idArticulo
    
    def getPrecioBase(self):
        return self.__precioBase
    
    def getUnidExistente(self):
        return self.__unidExistencia  

class Bebidas(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    
    def setCantUnidad(self,cantidad:str):
        self.__cantUnidad=cantidad
    
    def setProveedor(self,proveedor:str):
        self.__proveedor=proveedor

    def getCantUnidad(self):
        return self.__cantUnidad
    
    def getProveedor(self):
        return self.__proveedor

    def precioFinal(self):
        precio = self.getPrecioBase()*1.19
        return round(precio,2)

class Lacteos(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    
    def setCantUnidad(self,cantidad:str):
        self.__cantUnidad=cantidad
    
    def setProveedor(self,proveedor:str):
        self.__proveedor=proveedor

    def getCantUnidad(self):
        return self.__cantUnidad
    
    def getProveedor(self):
        return self.__proveedor

    def precioFinal(self):
        precio = self.getPrecioBase()*1.05
        return round(precio,2)

class Condimentos(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    
    def setCantUnidad(self,cantidad:str):
        self.__cantUnidad=cantidad
    
    def setProveedor(self,proveedor:str):
        self.__proveedor=proveedor

    def getCantUnidad(self):
        return self.__cantUnidad
    
    def getProveedor(self):
        return self.__proveedor
    
    def precioFinal(self):
        precio = self.getPrecioBase()
        return precio

def precioVenta(obj):
    return obj.precioFinal()

def lectura():
    n = open('Catalogo.csv','rt')
    data = [[],[],[]]
    linea = n.readline().rstrip('\n').split(',')
    while linea != ['']:
        if linea[3]=='Bebidas':
            obj=Bebidas()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5].rstrip('USD')))
            obj.setUnidExistente(int(linea[6]))
            obj.setCantUnidad(linea[4])
            obj.setProveedor(linea[2])
            data[0].append(obj)
        elif linea[3]=='Condimentos':
            obj=Condimentos()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5].rstrip('USD')))
            obj.setUnidExistente(int(linea[6]))
            obj.setCantUnidad(linea[4])
            obj.setProveedor(linea[2])
            data[1].append(obj)
        elif linea[3]=='LÃ¡cteos':
            obj=Lacteos()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5].rstrip('USD')))
            obj.setUnidExistente(int(linea[6]))
            obj.setCantUnidad(linea[4])
            obj.setProveedor(linea[2])
            data[2].append(obj)
        linea = n.readline().rstrip('\n').split(',')
    n.close()
    print(data[0][1].getPrecioBase())
    return data

def facturar(data):
    carrito=[[],[],[]]
    item=input('Id del Articulo: ')
    while item != 'fin':
        for i in range(3):
            for j in data[i]:
                if (j.getIdArticulo()==int(item)) and (j.getUnidExistente()>0):
                    carrito[i].append(j)
                    j.setUnidExistente(j.getUnidExistente()-1)
                elif (j.getIdArticulo()==int(item)) and (j.getUnidExistente()<=0):
                    print('Existencia insuficiente')

        item=input('Id del Articulo: ')
    return carrito
                
def imprimir(carrito):
    titulos=['Bebidas ....','Condimentos ','Lácteos ....']
    venta=0
    total=0

    print('\n----------------------------------')
    print('-------Super Max Economico -------')
    print('----------------------------------\n')
    print('Categoria   Cantidad    Precio Acu')
    for i in range(3):
        for j in carrito[i]:
            total += precioVenta(j)
            # print(j)
            # x=input('x')
        venta+=total
        print( f'{titulos[i]}.... {len(carrito[i])}...... {total}USD')
        total=0
    print(f'venta total: ........... {round(venta,2)}USD\n')

def main():
    data=lectura()
    carrito=facturar(data)
    imprimir(carrito)


if __name__=="__main__":
    main()
