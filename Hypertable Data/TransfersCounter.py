def readTransfer(userID, pMonth):

    
    with open('transfers.txt', 'r') as f:
        lines = f.readlines()
        counter = 0

        for line in lines:
            if(len(line) > 50):
                currentid = line[:9]
                
                if(int(currentid) == userID):
                    
                    month = line[25:][:2]
                    
                    if(month[1] == "/"):
                        month = month[0]
                    
                    if(int(month) == pMonth):
                        counter = counter + 1     
    print("Cantidad de transacciones: " + str(counter))

def main():
    userID = input("Id del usuario: ")
    pMonth = input("Mes deseado: ")
    readTransfer(int(userID), int(pMonth))

main()
