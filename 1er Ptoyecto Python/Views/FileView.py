from Handler.FileHandler import FileHandler
from os import system
from Exceptions.FileException import FileException

#Clase responsable del menu de archivo
class FileView:

    def __init__(self):
        self.option = '0'
        self.flag = True
    
    #Metodo para las acciones del menu
    def menuFile(self):
        repository = []
        while(self.flag):
            system("cls")
            print("Elegir una opcion:")
            print("1.Cargar el archivo (debe estar en la misma carpeta que Main.py)")
            print("2.Salir")
            self.option = input()
            
            if(self.option == '1'):
                self.option = '0'
                print("\nIntroducir nombre archivo: ")
                fileName = input()
                if(fileName.find(".txt") != -1):
                    repository = FileHandler.readFile(fileName)
                    repository.createRepositorys()
                    print("Cargado con exito")
                    input()
                else:
                    raise FileException("La extension del archivo es incorrecta, asegurarse que sea .txt")

            
            elif(self.option == '2'):
                self.flag = False

            else:
                print("Opcion no valida")
                input()
            
            
        return repository
