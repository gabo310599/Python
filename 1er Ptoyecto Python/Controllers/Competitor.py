from datetime import time

#Clase que contendras los datos de un competidor.
class Competitor:
    
    def __init__(self, dataList):
        self.ci = dataList[0]
        self.lastName1 = dataList[1]
        self.lastName2 = dataList[2]
        self.name = dataList[3]
        self.secondName = dataList[4]
        self.sex = dataList[5]
        self.age = dataList[6]
        self.time = time(int(dataList[7]),int(dataList[8]),int(dataList[9]))
        