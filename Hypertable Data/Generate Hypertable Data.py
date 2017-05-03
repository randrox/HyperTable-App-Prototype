from random import randint  #para utilizar la funcion que genera un entero aleatoriamente
from random import uniform  #para utilizar la funcion que genera un float aleatoriamente
import time     #para las fechas
import random

"""
Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    
http://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates

"""

def generateUsers():
    fileNames = open('people.txt', 'w')
    fileLogin = open('login.txt', 'w')
    
    names = ["Daniel","Daniela","Alejandro","Alejandra","Pablo","Hugo","Alvaro","Sergio","Diego","Mario",
             "Maria","Carlos","Karla","Javier","Ana","Miguel","Samuel","Jorge","Jason","David",
             "Antonio","Alisson","Aaron","Martin","Oscar","Andres","Andrea","Luis","Lucia","Erick",
             "Rafael","Roberto","Olga","Isaac","Samanta","Fabiola","Kevin","Bryan","Shirley","Violeta",
             "Victoria","Claudio","Claudia","Patricia","Katherine","Lizeth","Mariana","Mariano","Jimena","Megan",
             "Cesar","Marcela","Marcelo","German","Gloria","Beatriz","Hernan","Lilliana","Isabel","Julio",
             "Julia","Gabriel","Gabriela","Bernardo","Horacio","Monica","Monserrath","Ingrid","Natalia","Marta"
             "Noemy","Gerardo","Adrian","Fabiola","Joseph","Sebastian","Joel","Emanuel","Marlon","Leandro",
             "Tatiana","Fernanda","Paola","Diego","Juan","Nelson","Andrey","Sharon","Steven","Arturo"]

    lastNames = ["Morales","Gamboa","Duran","Vasquez","Vargas","Rosales","Barrantes","Arce","Gonzalez","Bonilla",
                 "Ulloa","Montero","Avila","Hernandez","Ramirez","Benavidez","Alfaro","Cruz","Lopez","Romero",
                 "Reyes","Zuñiga","Solano","Cordero","Guevara","Quiros","Flores","Viquez","Mora","Rojas",
                 "Mendez","Marin","Garcia","Azofeifa","Fonseca","Fallas","Sanchez","Abarca","Venegas","Ruiz",
                 "Zamora","Moya","Calvo","Chaves","Montoya","Umaña","Aguilar","Fernandez","Quesada","Aguirre",
                 "Retana","Solis","Trejos","Salazar","Salas","Vega","Perez","Lobo","Chavarria","Muñoz",
                 "Torres","Aviles","Naranjo","Barquero","Rodriguez","Camacho","Villalobos","Soto","Araya","Garro",]

    result = ""
    DNIList = []
    login = ""

    for i in range (0,100):
        DNI = str(randint(1,7)) + ("%d%d%d%d%d%d%d%d" % (i//10000000%10, i//1000000%10, i//100000%10, i//10000%10, i//1000%10, i//100%10, i//10%10, i%10))
        DNIList.append(DNI)
        name = names[randint(0,len(names)-1)]
        lastName = lastNames[randint(0,len(lastNames)-1)]
        accountBalance = str(uniform(0, 3000000))
        fileNames.write(DNI + "\tpersonName\t" + name + "\n" +
                        DNI + "\tpersonLastName\t" + lastName + "\n" +
                        DNI + "\tpersonBalance\t" + accountBalance + "\n")
        
        fileLogin.write(DNI + "\tpassword\t" + "1234\n")

    generateTransfers(DNIList)

def generateTransfers(DNIList):
    result = ""
    fileTransfers = open('transfers.txt', 'w')
    for i in range (0,100):
        DNITransmitter = DNIList[randint(0,len(DNIList)-1)]
        date = str(randint(9,10))+ "/15/2017"
        amount = str(uniform(0, 3000000))
        DNIReceiver = DNIList[randint(0,len(DNIList)-1)]
        fileTransfers.write(DNITransmitter + "\ttransferAmount:" + date + "\t" + amount + "\n" +
                            DNITransmitter + "\tmoneyReceptor\t" + DNIReceiver + "\n")


def main():
    generateUsers()
    
main()
