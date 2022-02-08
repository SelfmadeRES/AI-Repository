#Opdracht 1 - Pyramide

#Schrijf een programma dat een piramide van variabele lengte afdrukt, zoals in het voorbeeld.
# Druk ieder character apart af. De gebruiker geeft aan hoe groot de piramide is.
# Implementeer je programma twee keer, de eerste keer met twee for loops, en daarna met twee while loops.
# Maak ook versies die de pyramide een andere kant op laten wijzen.

def pyramidFor():
    size = eval(input("Hoe groot? "))           #input voor pyramide grootte
    numberOfLines = 2 * size                    #aantal lines dat zal worden gebruikt
    for i in range(numberOfLines):              #for-loop die enters print en het aantal te zetten sterretjes berekent
        jlength = size - abs(size-i)
        for j in range(jlength):                #loop die sterretjes zet met berekende jlength
            print("*", end = "")
        print("\n", end = "")

#pyramidFor()

def pyramidWhile():
    size = eval(input("Hoe groot? "))           #zelfde functie als pyramidFor, maar met while loops
    numberOfLines = 2 * size
    i = 1
    while i <= numberOfLines:
        jlength = size - abs(size-i)
        j = 1
        while j <= jlength:
            print("*", end = "")
            j += 1
        print("\n", end = "")
        i += 1

#pyramidWhile()

def mirPyramidFor():                            #Deze mirrored functies zijn praktisch hetzelfde als de voorgaande, maar met 1 extra loop
    size = eval(input("Hoe groot? "))
    numberOfLines = 2 * size
    for i in range(numberOfLines):
        jlength = size - abs(size - i)
        for k in range(abs(size - i)):          #De extra loop plaats lege characters " " voor de sterretjes
            print(" ", end="")
        for j in range(jlength):
            print("*", end = "")
        print("\n", end = "")

mirPyramidFor()

def mirPyramidWhile():                          #Zelfde idee als hiervoor maar met while-loop
    size = eval(input("Hoe groot? "))
    numberOfLines = 2 * size
    i = 1
    while i <= numberOfLines:
        jlength = size - abs(size-i)
        j = 1
        k = 1
        while k <= abs(size-i):
            print(" ", end = "")
            k += 1
        while j <= jlength:
            print("*", end = "")
            j += 1
        print("\n", end = "")
        i += 1

mirPyramidWhile()