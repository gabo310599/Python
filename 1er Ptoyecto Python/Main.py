from Controllers.CompetitorRepository import CompetitorRepository
from os import system
from Views.FileView import FileView
from Views.ActionView import ActionView
from Exceptions.FileException import FileException

if __name__ == '__main__':

    #Limpiar consola e inicializar variables
    system("cls")
    option = '0'
    flag = True
    repository = CompetitorRepository()
    
    #Elegir menu
    while(flag):
        system("cls")
        print("Elegir una opcion:")
        print("1.Archivo")
        print("2.Acciones")
        print("3.Salir")
        option = input()

        #Desplegar menu para cargar
        try:
            if(option == '1'):
                option = '0'
                menu = FileView()
                repository = menu.menuFile() 
            
            elif(option == '2' ):
                option = '0'
                menu = ActionView()
                menu.menuActions(repository)
        
            elif(option == '3'):
                flag = False
            
            else:
                print("Opcion no valida")
                input()

        except FileException as e:
            system("cls")
            print("Error: ",e)
            print("\n")
            input("Presionar Enter")
        

    
    
    


 