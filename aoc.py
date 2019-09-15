import numpy
import matplotlib.pyplot as plt
import networkx as nx


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

class Mapa:
    '''Clase contenedora de las ciudades, así como la distancia entre ellas,
    feremonas, así como la visibilidad.
    '''
    def __init__(self, nCity):
        self.nCity = nCity
        self.cityDistance = numpy.random.randint(0,nCity,size=(nCity,nCity))
        for i in range(nCity):
            for j in range(i+1, nCity):
                if self.cityDistance[i,j] != self.cityDistance[j,i]:
                    temp = self.cityDistance[i,j]
                    self.cityDistance[j,i] = temp
        numpy.fill_diagonal(self.cityDistance,0)
        self.visibilityMap = self.cityDistance
        self.visibilityMap = numpy.divide(1,self.cityDistance)
               

if __name__ == "__main__":


    aguascalientes = Mapa(11)
    print(aguascalientes.cityDistance)
    print(aguascalientes.visibilityMap)

    # rows, cols = numpy.where(matrizDistancia)
    # edges = zip(rows.tolist(), cols.tolist())
    # gr = nx.Graph()
    # gr.add_edges_from(edges)
    # labelsVec = {0:'1', 1:'2', 2:'3',3:'4',4:'5',
    #     5:'6',6:'7',7:'8',8:'9',9:'10',10:'11'}
    # plt.title('Conexión entre ciudades.') 
    # nx.draw(gr, labels=labelsVec, with_labels=True)
    # plt.show()




