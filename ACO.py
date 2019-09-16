import numpy
import random
import matplotlib.pyplot as plt
import networkx as nx


class Map:
    '''Clase contenedora de las ciudades, así como la distancia entre ellas,
    feremonas, así como la visibilidad.
    '''
    def __init__(self, nCity):
        self.nCity = nCity
        self.nIteration = numpy.random.randint(1,high=self.nCity)
        self.evaporation = numpy.random.random_sample()
        self.alpha = numpy.random.randint(1,high=self.nCity)
        self.beta = numpy.random.randint(1,high=self.nCity)
        self.tabuMatrix = []

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

    def createVisibilityMap(self):
        self.visibilityMap = numpy.zeros([self.nCity, self.nCity])
        for i in range(self.nCity):
            for j in range(i + 1, self.nCity):
                if self.cityDistance[i,j] != 0:
                    self.visibilityMap[i,j] = 1 / self.cityDistance[i,j] 
                    self.visibilityMap[j,i] = 1 / self.cityDistance[i,j] 

    def createAntColony(self, nAnt):
        self.nAnt = nAnt
        self.tabuMatrix = numpy.full((self.nAnt,self.nCity), 0)
        self.traveledDistance = numpy.full(self.nAnt, 0)
 
    def tabuList(self):
        startMap = random.sample(range(0, self.nCity), self.nAnt)
        for i in range(0, self.nAnt):
            self.tabuMatrix[i][0] = startMap[i]

    def plotCityMap(self):
        rows, cols = numpy.where(self.cityDistance)
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph()
        gr.add_edges_from(edges)
        labelsVec = {0:'1', 1:'2', 2:'3',3:'4',4:'5',
            5:'6',6:'7',7:'8',8:'9',9:'10',10:'11'}
        plt.title('Conexión entre ciudades.') 
        nx.draw(gr, labels=labelsVec, with_labels=True)
        plt.show()

    def startACO(self):
        self.createCityMap()
        self.createFeroMap()
        self.createVisibilityMap()
        print(f'Número de ciudades: {len(self.cityDistance)}')
        print(f'Número de iteraciones a realizar: {self.nIteration}')
        print(f'Valor de evaporación: {self.evaporation}')
        print(f'Importancía de la feromona (alpha): {self.alpha}')
        print(f'Importancía de la visibilidad (beta): {self.beta}')
        print(f'Matriz distancía entre ciudades: \n {self.cityDistance}')
        self.createAntColony(numpy.random.randint(1, high = self.nCity))
        print(f'Número de hormigas: {self.nAnt}')
        print(f'Lista Tabu: \n {self.tabuMatrix}')
        #self.plotCityMap()
        
        bestGlobal = 10000
        for i in range(self.nIteration):
            self.createJourney()
            bestPath = self.selectBestPath()
            if bestPath[1,0] < bestGlobal:
                pathGlobal = bestGlobal[0][0]
                bestGlobal = bestPath[1][0]
            self.feroMap *= self.evaporation
        print(f'El camino generado es: {pathGlobal} con el costo de: {bestGlobal}')

    def createJourney(self):
        self.tabuList()   
        for i in range(self.nAnt):
            visited = numpy.full(self.nCity, False)
            visited[self.tabuMatrix[i,0]] = True
            for j in range(self.nCity - 1):
                selected = self.nextCity(self.tabuMatrix[i,j], visited)
                visited[selected] = True
                self.tabuMatrix[i,j+1] = selected
            self.traveledDistance[i] = self.getDistance(self.tabuMatrix[i])
            self.updateFero(self.tabuMatrix[i], self.traveledDistance[i])

    def getDistance(self, path):
        total = 0
        current = path[0]
        for i in range(1, len(path)):
            total += self.cityDistance[current][path[i]]
            current = path[i]
        return total

    def selectBestPath(self):
        pathDistance = []
        self.tabuMatrix = self.tabuMatrix[numpy.argsort(self.traveledDistance)]
        self.traveledDistance = self.traveledDistance[numpy.argsort(self.traveledDistance)]
        pathDistance.append(self.tabuMatrix)
        pathDistance.append(self.traveledDistance)
        return pathDistance

    
    def nextCity(self, current, visited):
        possiblePath = []
        for i in range(self.nCity):
            if self.cityDistance[current][i] != 0 and visited[i] == False:
                possiblePath.append(i)
        jCandidate = 0
        candidateList = []
        for i in range(len(possiblePath)):
            probability = ((self.feroMap[current][possiblePath[i]]) ** self.alpha) *\
                ((self.visibilityMap[current][possiblePath[i]]) ** self.beta)
            jCandidate += probability
            candidateList.append(probability)     
        randomSelection = random.random()
        posibilityQueue = 0
        for i in range(len(possiblePath)):
            posibilityQueue += candidateList[i] / jCandidate
            if posibilityQueue > randomSelection:
                break
        return possiblePath



    
    def updateFero(self, ant, cost):
        start = ant[0]
        for i in range(self.nCity):
            self.feroMap[start][ant[i]] += 1/cost
            start = ant[i]

def main():
    aguascalientes = Map(11)   
    aguascalientes.startACO()
    



if __name__ == "__main__":
    main()





