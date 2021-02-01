"""Opdracht 1
Schrijf een programma dat een piramide van variabele lengte indrukt, zoals in het voorbeeld. Druk ieder character
apart af. De gebruiker geeft aan hoe groot de piramide is. Implementeer je programma twee keer, de eerste keer met
twee for loops, en daarna met twee while loops. Maak ook versies die de pyramide een andere kant op laten wijzen."""

def forLoopPyramid(teken):
    grootte = int(input("Hoe groot? "))
    tekenString = ""
    for i in range(2 * grootte + 1):
        for j in range(1, i):
            if j < 6:
                tekenString += teken
            else:
                tekenString = tekenString[:-1]
        print(tekenString)
        tekenString = ""


#forLoopPyramid("*")

def whileLoopPyramid(teken):
    grootte = int(input("Hoe groot? "))
    i = 0
    j = 0
    tekenString = ""
    while i < (grootte * 2):
        while j < i:
            if j < grootte:
                tekenString += teken
            else:
                tekenString = tekenString[:-1]
            j += 1
        print(tekenString)
        j = 0
        tekenString = ""
        i += 1

#whileLoopPyramid("*")

def forLoopInverted(teken):
    grootte = int(input("Hoe groot? "))
    tekenString = ""
    for i in range(1, grootte * 2 + 1):
        for j in range(1, grootte + 1):
            if len(tekenString) < abs((grootte - i)):
                tekenString += " "
            else:
                tekenString += teken
        print(tekenString)
        tekenString = ""

#forLoopInverted("*")

def whileLoopInverted(teken):
    grootte = int(input("Hoe groot? "))
    i = 0
    j = 0
    tekenString = ""
    while i < (grootte * 2):
        while j < grootte:
            if j < abs((grootte - i)):
                tekenString += " "
            else:
                tekenString += teken
            j += 1
        print(tekenString)
        j = 0
        tekenString = ""
        i += 1

#whileLoopInverted("*")