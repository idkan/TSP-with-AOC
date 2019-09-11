import numpy
import matplotlib.pyplot as plt


class Ciudad:
    '''
    Clase contenedora de distancia entre ciudades, visibilidad y feromonas.
    '''
    def crearCiudad(self, nCity):
        print(nCity)

class Hormiga:
    '''
    Clase contenedora de creación y caminos de hormigas.add()
    '''
if __name__ == "__main__":

    aguascalientes = Ciudad.crearCiudad(11)
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

    # rows, cols = numpy.where(matrizDistancia)
    # edges = zip(rows.tolist(), cols.tolist())
    # gr = nx.Graph()
    # gr.add_edges_from(edges)
    # labelsVec = {0:'1', 1:'2', 2:'3',3:'4',4:'5',
    #     5:'6',6:'7',7:'8',8:'9',9:'10',10:'11'}
    # plt.title('Conexión entre ciudades.') 
    # nx.draw(gr, labels=labelsVec, with_labels=True)
    # plt.show()




