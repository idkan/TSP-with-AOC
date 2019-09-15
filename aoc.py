import numpy
import matplotlib.pyplot as plt


    # matrizDistancia = [
    #     [0,8,7,0,3,0,0,0,0,7,5],
    #     [8,0,0,0,0,4,0,0,4,5,4],
    #     [7,0,0,0,6,0,0,7,0,0,0], 
    #     [0,0,0,0,0,0,2,0,3,0,0],
    #     [3,0,6,0,0,5,0,5,0,0,4],
    #     [0,4,0,0,5,0,3,5,3,0,1],
    #     [0,0,0,2,0,3,0,5,3,0,0],
    #     [0,0,7,0,5,5,5,0,0,0,0],
    #     [0,4,0,3,0,3,3,0,0,0,0],
    #     [7,5,0,0,0,0,0,0,0,0,0],
    #     [5,4,0,0,4,1,0,0,0,0,0]
    # ]

class Map:
    '''Clase contenedora de las ciudades, así como la distancia entre ellas,
    feremonas, así como la visibilidad.
    '''
    def __init__(self, nCity):
        self.nCity = nCity
    
    def createCityMap(self):
        self.cityDistance = numpy.random.randint(0,self.nCity,size=(self.nCity, self.nCity))
        for i in range(self.nCity):
            for j in range(i + 1, self.nCity):
                if self.cityDistance[i,j] != self.cityDistance[j,i]:
                    temp = self.cityDistance[i,j]
                    self.cityDistance[j,i] = temp
        numpy.fill_diagonal(self.cityDistance,0)

    def createFeroMap(self):
        self.feroMap = numpy.zeros([self.nCity, self.nCity])
        for i in range(self.nCity):
            for j in range(i + 1, self.nCity):
                if self.cityDistance[i,j] != 0:
                    self.feroMap[i,j] = 0.01
                    self.feroMap[j,i] = 0.01




class Ant:
    '''
    Clase contenedora para el recorrido de las hormigas, así como
    depositar feromonas en el camino.
    '''
    def __init__(self, nAnt):
        self.nAnt = nAnt

def main():
    aguascalientes = Map(11)   
    aguascalientes.createCityMap() 
    aguascalientes.createFeroMap()
    print(aguascalientes.cityDistance)
    print('---------------------------')
    print(aguascalientes.feroMap)

if __name__ == "__main__":
    main()

    # rows, cols = numpy.where(matrizDistancia)
    # edges = zip(rows.tolist(), cols.tolist())
    # gr = nx.Graph()
    # gr.add_edges_from(edges)
    # labelsVec = {0:'1', 1:'2', 2:'3',3:'4',4:'5',
    #     5:'6',6:'7',7:'8',8:'9',9:'10',10:'11'}
    # plt.title('Conexión entre ciudades.') 
    # nx.draw(gr, labels=labelsVec, with_labels=True)
    # plt.show()




