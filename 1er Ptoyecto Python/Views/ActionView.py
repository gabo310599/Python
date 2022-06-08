from Handler.FileHandler import FileHandler
from os import system

#Clase responsable del menu acciones
class ActionView:

    def __init__(self):
        self.option = '0'
        self.flag = True
    
    def menuActions(self, repository):
        while(self.flag):
            system("cls")
            print("Elegir una opcion:")
            print("1.Lista con la totalidad de participantes")
            print("2.Cantidad total de participantes")
            print("3.Cantidad de participantes por grupo etario")
            print("4.Cantidad de participantes por sexo")
            print("5.Ganadores por grupo etario")
            print("6.Ganadores por sexo")
            print("7.Ganadores por grupo etario y sexo")
            print("8.Ganador general")
            print("9.Histograma de participante por grupo etario")
            print("10.Promedio de tiempo por grupo etario y sexo")
            print("11.Salir")
            self.option = input()

            if(self.option == '1'):
                self.option = '0'
                repository.printCompetitors()
                input()
            
            elif(self.option == '2'):
                self.option = '0'
                repository.printTotalCompetitors()
                input()
            
            elif(self.option == '3'):
                self.option = '0'
                repository.printTotalEtarios()
                input()

            elif(self.option == '4'):
                self.option = '0'
                repository.printTotalGender()
                input()
            
            elif(self.option == '5'):
                self.option = '0'
                repository.printWinnersEtarios()
                input()
            
            elif(self.option == '6'):
                self.option = '0'
                repository.printWinnersGender()
                input()
            
            elif(self.option == '7'):
                self.option = '0'
                repository.printWinnersEG()
                input()
            
            elif(self.option == '8'):
                self.option = '0'
                repository.printWinners()
                input()
            
            elif(self.option == '9'):
                self.option = '0'
                repository.printHistogram()
                input()
            
            elif(self.option == '10'):
                self.option = '0'
                repository.timeAverage()
                input()
            
            elif(self.option == '11'):
                self.flag = False

            else:
                print("Opcion no valida")
                input()