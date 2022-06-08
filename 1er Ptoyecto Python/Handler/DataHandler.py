from Controllers.CompetitorRepository import CompetitorRepository
from Exceptions.FileException import FileException

#Clase que maneja la data extraida del archivo
class DataHandler:

    def __init__(self, repository = []):
        self.repository = CompetitorRepository()

    #Metodo que transforma una linea de data en un competidor
    def lineHandler(self,data):       
        for line in data:
            dataList = line.split(",")

            if(len(dataList) == 10):    
                if("\n" in dataList[9]):
                    dataList[9] = dataList[9].rstrip()  

                self.repository.addCompetitor(dataList)
            else: 
                raise FileException("La data del archivo no cumple con el numero de columnas necesarias")
        
        return self.repository
    

