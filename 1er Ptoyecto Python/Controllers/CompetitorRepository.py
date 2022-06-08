from Controllers.Competitor import Competitor
from os import system
from datetime import time
import math

#Clase que crea un repositorio de todos los competidores
class CompetitorRepository:

    def __init__(self):
        self.competitors = []
        self.juniorsM = []
        self.seniorsM = []
        self.mastersM = []
        self.juniorsF = []
        self.seniorsF = []
        self.mastersF = []
        self.male = []
        self.female = []
        self.juniors = []
        self.seniors = []
        self.masters = []

    #Agregar un competidor a la lista
    def addCompetitor(self, dataList):
        person = Competitor(dataList)
        self.competitors.append(person)

    #Crear repositorios juniors, seniors, masters y por edades
    def createRepositorys(self):
        for i in range(0,len(self.competitors)):

            if(self.competitors[i].sex == 'M'):
                self.male.append(self.competitors[i])
                if(int(self.competitors[i].age) <= 25):
                    self.juniorsM.append(self.competitors[i])
                    self.juniors.append(self.competitors[i])
                if(int(self.competitors[i].age) > 25 and int(self.competitors[i].age) <= 40):
                    self.seniorsM.append(self.competitors[i])
                    self.seniors.append(self.competitors[i])
                if(int(self.competitors[i].age) > 40):
                    self.mastersM.append(self.competitors[i])
                    self.masters.append(self.competitors[i])

            if(self.competitors[i].sex == 'F'):
                self.female.append(self.competitors[i])
                if(int(self.competitors[i].age) <= 25):
                    self.juniorsF.append(self.competitors[i])
                    self.juniors.append(self.competitors[i])
                if(int(self.competitors[i].age) > 25 and int(self.competitors[i].age) <= 40):
                    self.seniorsF.append(self.competitors[i])
                    self.seniors.append(self.competitors[i])
                if(int(self.competitors[i].age) > 40):
                    self.mastersF.append(self.competitors[i])
                    self.masters.append(self.competitors[i])
    
    #Metodo que imprime una tabla con todos los competidores
    def printCompetitors(self):
        system("cls")
        print("{:<10} {:<23} {:<24} {:<14} {:<22} {:<12} {:<12} {:<13}".format(
            "CI",
            "Primer Apellido",
            "Segundo Apellido",
            "Nombre",
            "Inicial Nombre 2",
            "Sexo",
            "Edad",
            "Tiempo"))
        print("\n")
        for person in self.competitors:
            print("{:<10} {:<23} {:<24} {:<14} {:<22} {:<12} {:<12} {:<13}".format(
                person.ci,
                person.lastName1,
                person.lastName2,
                person.name,
                person.secondName,
                person.sex,
                person.age,
                str(person.time)
            ))
        print("\nPresionar Enter")
    
    #Metodo que devuelve la cantidad total de participantes
    def printTotalCompetitors(self):
        system("cls")
        total = 0

        for i in range(0,len(self.competitors)):
            total = total+1
        
        print("Cantidad total de participantes: "+str(total))
        print("\nPresionar Enter")

    #Metodo que imprime los participantes por grupo etario
    def printTotalEtarios(self):
        system("cls")
        totalJuniors = 0
        totalSeniors = 0
        totalMasters = 0

        for i in range(0,len(self.juniors)):
            totalJuniors = totalJuniors+1
        for i in range(0,len(self.seniors)):
            totalSeniors = totalSeniors+1
        for i in range(0,len(self.masters)):
            totalMasters = totalMasters+1

        print("{:<15} {:<15}".format("Grupo","Cantidad"))
        print("\n")
        print("{:<15} {:<15}".format("Juniors",str(totalJuniors)))
        print("{:<15} {:<15}".format("Seniors",str(totalSeniors)))
        print("{:<15} {:<15}".format("Masters",str(totalMasters)))
        print("\nPresionar Enter")
    
    #Metodo que imprime los participantes por grupo de generos
    def printTotalGender(self):
        system("cls")
        totalMale = 0
        totalFemale = 0

        for i in range(0,len(self.male)):
            totalMale = totalMale+1
        for i in range(0,len(self.female)):
            totalFemale = totalFemale+1
        
        print("Total participantes masculino: "+str(totalMale)+". Total participantes femenino: "+str(totalFemale))
        print("\nPresionar Enter")

    #Metodo que imprime los tres primeros puestos por grupo etarios
    def printWinnersEtarios(self):
        system("cls")
        dataList = [None,None,None,None,None,None,None,'23','59','59']
        firstJuniors = Competitor(dataList)
        secondJuniors = Competitor(dataList)
        thirdJuniors = Competitor(dataList)
        firstSeniors = Competitor(dataList)
        secondSeniors = Competitor(dataList)
        thirdSeniors = Competitor(dataList)
        firstMasters = Competitor(dataList)
        secondMasters = Competitor(dataList)
        thirdMasters = Competitor(dataList)
        
        #Determino los tres primeros juniors
        for person in self.juniors:
            if(person.time <= firstJuniors.time):
                aux1 = firstJuniors
                aux2 = secondJuniors
                firstJuniors = person
                secondJuniors = aux1
                thirdJuniors = aux2
            elif(person.time <= secondJuniors.time):
                aux2 = secondJuniors
                secondJuniors = person
                thirdJuniors = aux2
            elif(person.time <= thirdJuniors.time):
                thirdJuniors = person
        
        #Determino los tres primeros seniors
        for person in self.seniors:
            if(person.time <= firstSeniors.time):
                aux1 = firstSeniors
                aux2 = secondSeniors
                firstSeniors = person
                secondSeniors = aux1
                thirdSeniors = aux2
            elif(person.time <= secondSeniors.time):
                aux2 = secondSeniors
                secondSeniors = person
                thirdSeniors = aux2
            elif(person.time <= thirdSeniors.time):
                thirdSeniors = person
        
        #Determino los tres primeros masters
        for person in self.masters:
            if(person.time <= firstMasters.time):
                aux1 = firstMasters
                aux2 = secondMasters
                firstMasters = person
                secondMasters = aux1
                thirdMasters = aux2
            elif(person.time <= secondMasters.time):
                aux2 = secondMasters
                secondMasters = person
                thirdMasters = aux2
            elif(person.time <= thirdMasters.time):
                thirdMasters = person
        
        print("\n")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Posicion",
            "Grupo",
            "CI",
            "Nombre",
            "Apellido",
            "Edad",
            "Tiempo"))
        print("\n")

        #Juniors
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Juniors",
            firstJuniors.ci,
            firstJuniors.name,
            firstJuniors.lastName1,
            firstJuniors.age,
            str(firstJuniors.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Juniors",
            secondJuniors.ci,
            secondJuniors.name,
            secondJuniors.lastName1,
            secondJuniors.age,
            str(secondJuniors.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Juniors",
            thirdJuniors.ci,
            thirdJuniors.name,
            thirdJuniors.lastName1,
            thirdJuniors.age,
            str(thirdJuniors.time)))
        print("\n")
        
        #Seniors
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Seniors",
            firstSeniors.ci,
            firstSeniors.name,
            firstSeniors.lastName1,
            firstSeniors.age,
            str(firstSeniors.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Seniors",
            secondSeniors.ci,
            secondSeniors.name,
            secondSeniors.lastName1,
            secondSeniors.age,
            str(secondSeniors.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Seniors",
            thirdSeniors.ci,
            thirdSeniors.name,
            thirdSeniors.lastName1,
            thirdSeniors.age,
            str(thirdSeniors.time)))
        print("\n")
        
        #Masters
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Masters",
            firstMasters.ci,
            firstMasters.name,
            firstMasters.lastName1,
            firstMasters.age,
            str(firstMasters.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Masters",
            secondMasters.ci,
            secondMasters.name,
            secondMasters.lastName1,
            secondMasters.age,
            str(secondMasters.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Masters",
            thirdMasters.ci,
            thirdMasters.name,
            thirdMasters.lastName1,
            thirdMasters.age,
            str(thirdMasters.time)))
        print("\n")

        print("\nPresionar Enter")
    
    ##Metodo que imprime los ganadores por grupo de generos
    def printWinnersGender(self):
        system("cls")
        dataList = [None,None,None,None,None,None,None,'23','59','59']
        firstMale = Competitor(dataList)
        secondMale = Competitor(dataList)
        thirdMale = Competitor(dataList)
        firstFemale = Competitor(dataList)
        secondFemale = Competitor(dataList)
        thirdFemale = Competitor(dataList)

        #Determino los tres primeros masculinos
        for person in self.male:
            if(person.time <= firstMale.time):
                aux1 = firstMale
                aux2 = secondMale
                firstMale = person
                secondMale = aux1
                thirdMale = aux2
            elif(person.time <= secondMale.time):
                aux2 = secondMale
                secondMale = person
                thirdMale = aux2
            elif(person.time <= thirdMale.time):
                thirdMale = person
        
        #Determino los tres primeros femeninos
        for person in self.female:
            if(person.time <= firstFemale.time):
                aux1 = firstFemale
                aux2 = secondFemale
                firstFemale = person
                secondFemale = aux1
                thirdFemale = aux2
            elif(person.time <= secondFemale.time):
                aux2 = secondFemale
                secondFemale = person
                thirdFemale = aux2
            elif(person.time <= thirdFemale.time):
                thirdFemale = person

        print("\n")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Posicion",
            "Genero",
            "CI",
            "Nombre",
            "Apellido",
            "Tiempo"))
        print("\n")

        #Maculino
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            firstMale.sex,
            firstMale.ci,
            firstMale.name,
            firstMale.lastName1,
            str(firstMale.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            secondMale.sex,
            secondMale.ci,
            secondMale.name,
            secondMale.lastName1,
            str(secondMale.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            thirdMale.sex,
            thirdMale.ci,
            thirdMale.name,
            thirdMale.lastName1,
            str(thirdMale.time)))
        print("\n")
        
        #Femenino
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            firstFemale.sex,
            firstFemale.ci,
            firstFemale.name,
            firstFemale.lastName1,
            str(firstFemale.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            secondFemale.sex,
            secondFemale.ci,
            secondFemale.name,
            secondFemale.lastName1,
            str(secondFemale.time)))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            thirdFemale.sex,
            thirdFemale.ci,
            thirdFemale.name,
            thirdFemale.lastName1,
            str(thirdFemale.time)))
        print("\n")

        print("\nPresionar Enter")
    
    #Metodo que determina ganadores por grupos etarios y de genero
    def printWinnersEG(self):
        system("cls")
        dataList = [None,None,None,None,None,None,None,'23','59','59']
        firstJuniorsM = Competitor(dataList)
        secondJuniorsM = Competitor(dataList)
        thirdJuniorsM = Competitor(dataList)
        firstSeniorsM = Competitor(dataList)
        secondSeniorsM = Competitor(dataList)
        thirdSeniorsM = Competitor(dataList)
        firstMastersM = Competitor(dataList)
        secondMastersM = Competitor(dataList)
        thirdMastersM = Competitor(dataList)
        firstJuniorsF = Competitor(dataList)
        secondJuniorsF = Competitor(dataList)
        thirdJuniorsF = Competitor(dataList)
        firstSeniorsF = Competitor(dataList)
        secondSeniorsF = Competitor(dataList)
        thirdSeniorsF = Competitor(dataList)
        firstMastersF = Competitor(dataList)
        secondMastersF = Competitor(dataList)
        thirdMastersF = Competitor(dataList)

        #Determino los tres primeros masculinos juniors
        for person in self.juniorsM:
            if(person.time <= firstJuniorsM.time):
                aux1 = firstJuniorsM
                aux2 = secondJuniorsM
                firstJuniorsM = person
                secondJuniorsM = aux1
                thirdJuniorsM = aux2
            elif(person.time <= secondJuniorsM.time):
                aux2 = secondJuniorsM
                secondJuniorsM = person
                thirdJuniorsM = aux2
            elif(person.time <= thirdJuniorsM.time):
                thirdJuniorsM = person
        
        #Determino los tres primeros masculinos seniors
        for person in self.seniorsM:
            if(person.time <= firstSeniorsM.time):
                aux1 = firstSeniorsM
                aux2 = secondSeniorsM
                firstSeniorsM = person
                secondSeniorsM = aux1
                thirdSeniorsM = aux2
            elif(person.time <= secondSeniorsM.time):
                aux2 = secondSeniorsM
                secondSeniorsM = person
                thirdSeniorsM = aux2
            elif(person.time <= thirdSeniorsM.time):
                thirdSeniorsM = person
        
        #Determino los tres primeros masculinos masters
        for person in self.mastersM:
            if(person.time <= firstMastersM.time):
                aux1 = firstMastersM
                aux2 = secondMastersM
                firstMastersM = person
                secondMastersM = aux1
                thirdMastersM = aux2
            elif(person.time <= secondMastersM.time):
                aux2 = secondMastersM
                secondMastersM = person
                thirdMastersM = aux2
            elif(person.time <= thirdMastersM.time):
                thirdMastersM = person
        
        #Determino los tres primeros femeninos juniors
        for person in self.juniorsF:
            if(person.time <= firstJuniorsF.time):
                aux1 = firstJuniorsF
                aux2 = secondJuniorsF
                firstJuniorsF = person
                secondJuniorsF = aux1
                thirdJuniorsF = aux2
            elif(person.time <= secondJuniorsF.time):
                aux2 = secondJuniorsF
                secondJuniorsF = person
                thirdJuniorsF = aux2
            elif(person.time <= thirdJuniorsF.time):
                thirdJuniorsF = person
        
        #Determino los tres primeros femeninos seniors
        for person in self.seniorsF:
            if(person.time <= firstSeniorsF.time):
                aux1 = firstSeniorsF
                aux2 = secondSeniorsF
                firstSeniorsF = person
                secondSeniorsF = aux1
                thirdSeniorsF = aux2
            elif(person.time <= secondSeniorsF.time):
                aux2 = secondSeniorsF
                secondSeniorsF = person
                thirdSeniorsF = aux2
            elif(person.time <= thirdSeniorsF.time):
                thirdSeniorsF = person

        #Determino los tres primeros femeninos masters
        for person in self.mastersF:
            if(person.time <= firstMastersF.time):
                aux1 = firstMastersF
                aux2 = secondMastersF
                firstMastersF = person
                secondMastersF = aux1
                thirdMastersF = aux2
            elif(person.time <= secondMastersF.time):
                aux2 = secondMastersF
                secondMastersF = person
                thirdMastersF = aux2
            elif(person.time <= thirdMastersF.time):
                thirdMastersF = person

        print("\n")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Posicion",
            "Grupo",
            "Genero",
            "CI",
            "Nombre",
            "Apellido",
            "Tiempo"))
        print("\n")

        #Masculino juniors
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Juniors",
            firstJuniorsM.sex,
            firstJuniorsM.ci,
            firstJuniorsM.name,
            firstJuniorsM.lastName1,
            str(firstJuniorsM.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Juniors",
            secondJuniorsM.sex,
            secondJuniorsM.ci,
            secondJuniorsM.name,
            secondJuniorsM.lastName1,
            str(secondJuniorsM.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Juniors",
            thirdJuniorsM.sex,
            thirdJuniorsM.ci,
            thirdJuniorsM.name,
            thirdJuniorsM.lastName1,
            str(thirdJuniorsM.time)
        ))
        print("\n")

        #Masculino seniors
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Seniors",
            firstSeniorsM.sex,
            firstSeniorsM.ci,
            firstSeniorsM.name,
            firstSeniorsM.lastName1,
            str(firstSeniorsM.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Seniors",
            secondSeniorsM.sex,
            secondSeniorsM.ci,
            secondSeniorsM.name,
            secondSeniorsM.lastName1,
            str(secondSeniorsM.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Seniors",
            thirdSeniorsM.sex,
            thirdSeniorsM.ci,
            thirdSeniorsM.name,
            thirdSeniorsM.lastName1,
            str(thirdSeniorsM.time)
        ))
        print("\n")

        #Masculino masters
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Masters",
            firstMastersM.sex,
            firstMastersM.ci,
            firstMastersM.name,
            firstMastersM.lastName1,
            str(firstMastersM.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Masters",
            secondMastersM.sex,
            secondMastersM.ci,
            secondMastersM.name,
            secondMastersM.lastName1,
            str(secondMastersM.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Masters",
            thirdMastersM.sex,
            thirdMastersM.ci,
            thirdMastersM.name,
            thirdMastersM.lastName1,
            str(thirdMastersM.time)
        ))
        print("\n")

        #Femenino juniors
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Juniors",
            firstJuniorsF.sex,
            firstJuniorsF.ci,
            firstJuniorsF.name,
            firstJuniorsF.lastName1,
            str(firstJuniorsF.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Juniors",
            secondJuniorsF.sex,
            secondJuniorsF.ci,
            secondJuniorsF.name,
            secondJuniorsF.lastName1,
            str(secondJuniorsF.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Juniors",
            thirdJuniorsF.sex,
            thirdJuniorsF.ci,
            thirdJuniorsF.name,
            thirdJuniorsF.lastName1,
            str(thirdJuniorsF.time)
        ))
        print("\n")

        #Femenino seniors
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Seniors",
            firstSeniorsF.sex,
            firstSeniorsF.ci,
            firstSeniorsF.name,
            firstSeniorsF.lastName1,
            str(firstSeniorsF.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Seniors",
            secondSeniorsF.sex,
            secondSeniorsF.ci,
            secondSeniorsF.name,
            secondSeniorsF.lastName1,
            str(secondSeniorsF.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Seniors",
            thirdSeniorsF.sex,
            thirdSeniorsF.ci,
            thirdSeniorsF.name,
            thirdSeniorsF.lastName1,
            str(thirdSeniorsF.time)
        ))
        print("\n")

        #Femenino masters
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            "Masters",
            firstMastersF.sex,
            firstMastersF.ci,
            firstMastersF.name,
            firstMastersF.lastName1,
            str(firstMastersF.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            "Masters",
            secondMastersF.sex,
            secondMastersF.ci,
            secondMastersF.name,
            secondMastersF.lastName1,
            str(secondMastersF.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            "Masters",
            thirdMastersF.sex,
            thirdMastersF.ci,
            thirdMastersF.name,
            thirdMastersF.lastName1,
            str(thirdMastersF.time)
        ))
        print("\n")

        print("\nPresionar Enter")

    #Metodo que determina ganadores generales
    def printWinners(self):
        system("cls")
        dataList = [None,None,None,None,None,None,None,'23','59','59']
        first = Competitor(dataList)
        second = Competitor(dataList)
        third = Competitor(dataList)

        #Determino los tres primerosm 
        for person in self.competitors:
            if(person.time <= first.time):
                aux1 = first
                aux2 = second
                first = person
                second = aux1
                third = aux2
            elif(person.time <= second.time):
                aux2 = second
                second = person
                third = aux2
            elif(person.time <= third.time):
                third = person
        
        print("\n")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Posicion",
            "Genero",
            "CI",
            "Nombre",
            "Apellido",
            "Tiempo"))
        print("\n")

        #Ganadores
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "1ero",
            first.sex,
            first.ci,
            first.name,
            first.lastName1,
            str(first.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "2do",
            second.sex,
            second.ci,
            second.name,
            second.lastName1,
            str(second.time)
        ))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "3ero",
            third.sex,
            third.ci,
            third.name,
            third.lastName1,
            str(third.time)
        ))
        print("\n")

        print("\nPresionar Enter")
    
    #Metodo que imprime histograma por grupo etario
    def printHistogram(self):
        system("cls")
        totalJuniors = 0
        totalSeniors = 0
        totalMasters = 0

        for i in range(0,len(self.juniors)):
            totalJuniors = totalJuniors+1
        for i in range(0,len(self.seniors)):
            totalSeniors = totalSeniors+1
        for i in range(0,len(self.masters)):
            totalMasters = totalMasters+1
        
        total = totalJuniors+totalSeniors+totalMasters
        percentageJuniors = round((totalJuniors*100)/total)
        percentageSeniors = round((totalSeniors*100)/total)
        percentageMasters = round((totalMasters*100)/total)
        
        print(f"Juniors({totalJuniors}): |"+ "*"*percentageJuniors)
        print(f"Seniors({totalSeniors}): |"+ "*"*percentageSeniors) 
        print(f"Masters({totalMasters}): |"+ "*"*percentageMasters)    

        print("\n")

        print("\nPresionar Enter")   

    #Metodo que calcula promedio de tiempo por grupos 
    def timeAverage(self):
        system("cls")

        #Juniors masculinos
        totalHours = 0
        totalMinutes = 0
        totalSeconds = 0
        extraH = 0
        extraM = 0
        extraS = 0
        extra = 0
        hour = 0
        minute = 0
        second = 0
        cont = 0
        for person in self.juniorsM:
            totalHours = totalHours+int(person.time.hour)
            totalMinutes = totalMinutes+int(person.time.minute)
            totalSeconds = totalSeconds+int(person.time.second)
            cont = cont + 1
        
        totalHours = totalHours/cont
        totalMinutes = totalMinutes/cont
        totalSeconds = totalSeconds/cont

        extraH, hour = math.modf(totalHours)
        if(extraH < 0):
            totalMinutes = totalMinutes + extraH*60

        extraM, minute = math.modf(totalMinutes)
        if(extraM < 0):
            totalSeconds = totalSeconds + extraM*60
        
        extraS, second = math.modf(totalSeconds)
        
        if(second > 59):
            second = second/60
            second, extra = math.modf(second)
            second = second*60
            minute = minute+extra
        if(minute > 59):
            minute = minute/60
            minute, extra = math.modf(minute)
            minute = minute*60
            hour = hour+extra
          
        juniorsAverageM = time(int(hour),int(minute),int(second))

        #Seniors masculinos
        totalHours = 0
        totalMinutes = 0
        totalSeconds = 0
        extraH = 0
        extraM = 0
        extraS = 0
        extra = 0
        hour = 0
        minute = 0
        second = 0
        cont = 0
        for person in self.seniorsM:
            totalHours = totalHours+int(person.time.hour)
            totalMinutes = totalMinutes+int(person.time.minute)
            totalSeconds = totalSeconds+int(person.time.second)
            cont = cont + 1
        
        totalHours = totalHours/cont
        totalMinutes = totalMinutes/cont
        totalSeconds = totalSeconds/cont

        extraH, hour = math.modf(totalHours)
        if(extraH < 0):
            totalMinutes = totalMinutes + extraH*60

        extraM, minute = math.modf(totalMinutes)
        if(extraM < 0):
            totalSeconds = totalSeconds + extraM*60
        
        extraS, second = math.modf(totalSeconds)
        
        if(second > 59):
            second = second/60
            second, extra = math.modf(second)
            second = second*60
            minute = minute+extra
        if(minute > 59):
            minute = minute/60
            minute, extra = math.modf(minute)
            minute = minute*60
            hour = hour+extra
          
        seniorsAverageM = time(int(hour),int(minute),int(second))

        #Masters masculinos
        totalHours = 0
        totalMinutes = 0
        totalSeconds = 0
        extraH = 0
        extraM = 0
        extraS = 0
        extra = 0
        hour = 0
        minute = 0
        second = 0
        cont = 0
        for person in self.mastersM:
            totalHours = totalHours+int(person.time.hour)
            totalMinutes = totalMinutes+int(person.time.minute)
            totalSeconds = totalSeconds+int(person.time.second)
            cont = cont + 1
        
        totalHours = totalHours/cont
        totalMinutes = totalMinutes/cont
        totalSeconds = totalSeconds/cont

        extraH, hour = math.modf(totalHours)
        if(extraH < 0):
            totalMinutes = totalMinutes + extraH*60

        extraM, minute = math.modf(totalMinutes)
        if(extraM < 0):
            totalSeconds = totalSeconds + extraM*60
        
        extraS, second = math.modf(totalSeconds)
        
        if(second > 59):
            second = second/60
            second, extra = math.modf(second)
            second = second*60
            minute = minute+extra
        if(minute > 59):
            minute = minute/60
            minute, extra = math.modf(minute)
            minute = minute*60
            hour = hour+extra
          
        mastersAverageM = time(int(hour),int(minute),int(second))

        #Juniors femeninos
        totalHours = 0
        totalMinutes = 0
        totalSeconds = 0
        extraH = 0
        extraM = 0
        extraS = 0
        extra = 0
        hour = 0
        minute = 0
        second = 0
        cont = 0
        for person in self.juniorsF:
            totalHours = totalHours+int(person.time.hour)
            totalMinutes = totalMinutes+int(person.time.minute)
            totalSeconds = totalSeconds+int(person.time.second)
            cont = cont + 1
        
        totalHours = totalHours/cont
        totalMinutes = totalMinutes/cont
        totalSeconds = totalSeconds/cont

        extraH, hour = math.modf(totalHours)
        if(extraH < 0):
            totalMinutes = totalMinutes + extraH*60

        extraM, minute = math.modf(totalMinutes)
        if(extraM < 0):
            totalSeconds = totalSeconds + extraM*60
        
        extraS, second = math.modf(totalSeconds)
        
        if(second > 59):
            second = second/60
            second, extra = math.modf(second)
            second = second*60
            minute = minute+extra
        if(minute > 59):
            minute = minute/60
            minute, extra = math.modf(minute)
            minute = minute*60
            hour = hour+extra
          
        juniorsAverageF = time(int(hour),int(minute),int(second))

        #Seniors femeninos
        totalHours = 0
        totalMinutes = 0
        totalSeconds = 0
        extraH = 0
        extraM = 0
        extraS = 0
        extra = 0
        hour = 0
        minute = 0
        second = 0
        cont = 0
        for person in self.seniorsF:
            totalHours = totalHours+int(person.time.hour)
            totalMinutes = totalMinutes+int(person.time.minute)
            totalSeconds = totalSeconds+int(person.time.second)
            cont = cont + 1
        
        totalHours = totalHours/cont
        totalMinutes = totalMinutes/cont
        totalSeconds = totalSeconds/cont

        extraH, hour = math.modf(totalHours)
        if(extraH < 0):
            totalMinutes = totalMinutes + extraH*60

        extraM, minute = math.modf(totalMinutes)
        if(extraM < 0):
            totalSeconds = totalSeconds + extraM*60
        
        extraS, second = math.modf(totalSeconds)
        
        if(second > 59):
            second = second/60
            second, extra = math.modf(second)
            second = second*60
            minute = minute+extra
        if(minute > 59):
            minute = minute/60
            minute, extra = math.modf(minute)
            minute = minute*60
            hour = hour+extra
          
        seniorsAverageF = time(int(hour),int(minute),int(second))

        #Masters femeninos
        totalHours = 0
        totalMinutes = 0
        totalSeconds = 0
        extraH = 0
        extraM = 0
        extraS = 0
        extra = 0
        hour = 0
        minute = 0
        second = 0
        cont = 0
        for person in self.mastersF:
            totalHours = totalHours+int(person.time.hour)
            totalMinutes = totalMinutes+int(person.time.minute)
            totalSeconds = totalSeconds+int(person.time.second)
            cont = cont + 1
        
        totalHours = totalHours/cont
        totalMinutes = totalMinutes/cont
        totalSeconds = totalSeconds/cont

        extraH, hour = math.modf(totalHours)
        if(extraH < 0):
            totalMinutes = totalMinutes + extraH*60

        extraM, minute = math.modf(totalMinutes)
        if(extraM < 0):
            totalSeconds = totalSeconds + extraM*60
        
        extraS, second = math.modf(totalSeconds)
        
        if(second > 59):
            second = second/60
            second, extra = math.modf(second)
            second = second*60
            minute = minute+extra
        if(minute > 59):
            minute = minute/60
            minute, extra = math.modf(minute)
            minute = minute*60
            hour = hour+extra
          
        mastersAverageF = time(int(hour),int(minute),int(second))
        
        print("\n")
        print("{:<15} {:<15} {:<15}".format("Grupo", "Genero","Promedio"))
        print("\n")

        print("{:<15} {:<15} {:<15}".format("Juniors", "M",str(juniorsAverageM)))
        print("{:<15} {:<15} {:<15}".format("Seniors", "M",str(seniorsAverageM)))
        print("{:<15} {:<15} {:<15}".format("Masters", "M",str(mastersAverageM)))
        print("{:<15} {:<15} {:<15}".format("Juniors", "F",str(juniorsAverageF)))
        print("{:<15} {:<15} {:<15}".format("Seniors", "F",str(seniorsAverageF)))
        print("{:<15} {:<15} {:<15}".format("Masters", "F",str(mastersAverageF)))

        print("\n")

        print("\nPresionar Enter")

        
        

