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
def strTimeProp(start, end, format, prop):
    
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)


def generateUsers():
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

    for i in range (0,10):
        DNI = str(randint(111111111,777777777))
        DNIList.append(DNI)
        name = names[randint(0,len(names)-1)]
        lastName = lastNames[randint(0,len(lastNames)-1)]
        accountBalance = str(uniform(0, 3000000))
        result += DNI + "\t" + name + "\t" + lastName + "\t" + accountBalance + "\n"

    print(result)
    generateTransfers(DNIList)

def generateTransfers(DNIList):
    result = ""

    for i in range (0,10):
        DNITransmitter = DNIList[randint(0,len(DNIList)-1)]
        date = randomDate("1/1/2000 1:30 PM", "1/1/2017 4:50 AM", random.random())
        date = date[:-8]
        amount = str(uniform(0, 3000000))
        DNIReceiver = DNIList[randint(0,len(DNIList)-1)]
        result += DNITransmitter + "\t" + date + "\t" + amount + "\t" + DNIReceiver + "\n"

    print(result)

def main():
    generateUsers()
    
main()