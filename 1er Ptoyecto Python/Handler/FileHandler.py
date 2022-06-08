from Handler.DataHandler import DataHandler
from genericpath import exists
from Exceptions.FileException import FileException

#Clase que se dedica a manejar las acciones que se realizan sobre el archivo
class FileHandler:

    #Metodo que lee el archivo y retorna un repositorio con los competidores
    def readFile(fileName):
        
        if(exists(fileName)):
            f = open (fileName, 'r')
            x =  DataHandler()
            repository = x.lineHandler(f)
            f.close()

            return repository
        
        else:
            raise FileException("No se encontro el archivo, recuerda escribir la extension.")

    
        