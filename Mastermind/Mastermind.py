#mastermind
#imports
import random
import copy
import itertools


def spelkiezen():  #Deze functie laat de speler kiezen of hij wil raden of zetten. Als hij voor zetten kiest moet hij een code in formaat "CODE" kiezen
    spelsoort = input("Wil je raden of zetten: ")
    if spelsoort == "raden":
        return spelsoort
    elif spelsoort == "zetten":
        code = list(input("Wat is je code (R, O, Y, G, B, P): "))  #De toegestane kleuren zijn Red, Orange, Yellow, Green, BLue en Purple
        return code
    else:
        print("incorrect input, run opnieuw")
        exit()


def codezetten():  #Deze functie zal worden aangeroepen als de speler kiest voor raden. De functie genereert een random code.
    code = []
    codeletters = ["R", "O", "Y", "G", "B", "P"]
    for i in range(4):
        codegetal = random.randint(0, 5)
        codeletter = codeletters[codegetal]
        code.append(codeletter)
    return code

def raadbot(beurt, feedback):
    unchanged = ["R", "O", "Y", "G", "B", "P"]
    lettersleft = ["R", "O", "Y", "G", "B", "P"]
    ######start######
    if beurt == 1:
        gok = []
        for i in range(2):
            gokletter = random.choice(lettersleft)
            gok.append(gokletter)
            gok.append(gokletter)
            lettersleft.remove(gokletter)
    elif feedback == [] and beurt == 2:
        gok = []
        for i in range(2):
            gokletter = random.choice(letters)
            gok.append(gokletter)
            gok.append(gokletter)
            lettersleft.remove(gokletter)
    elif feedback == [] and beurt == 3:
        gok = []
        for i in range(2):
            gokletter = random.choice(letters)
            gok.append(gokletter)
            gok.append(gokletter)
    #####verder######
    reversedone = False
    if gok.count("WHITE") >= 2:
        gok.reverse()
        reversedone = True
    return gok
    #print(gok, [])

#raadbot(1)

def createPossibleCodes(colors, positions: int):
    listOfCombs = []
    for p in itertools.product(colors, repeat=positions): #itertools.product pakt alle mogelijkheden. https://stackoverflow.com/questions/14006867/python-itertools-permutations-how-to-include-repeating-characters
        listOfCombs.append(list(p))
    return listOfCombs


def codeControleren(code, guess):
    pins = []
    changedcode = code.copy()
    changedguess = guess.copy()
    j = 0
    for c in guess:
        if c == code[j]:
            pins.append("BLACK")
            changedcode.remove(c)
            changedguess.remove(c)
        j += 1
    for d in changedguess:
        if d in changedcode:
            pins.append("WHITE")
            changedcode.remove(d)
    pins.sort()
    if pins == ["BLACK", "BLACK", "BLACK", "BLACK"]:
        return "done"
    else:
        return pins

def pickGuess(combs):
    guess = random.choice(combs)
    return guess





def mainfunc():
    spel = spelkiezen()
    geraden = False
    if spel == "raden":
        code = codezetten() #De code wordt de code die random is gekozen
        pins = []   #Hier komen de pins die het antwoord geven
        for i in range(1, 13):
            changedcode = code.copy()
            print("Gok " + str(i) + ":")
            guess = list(input("Raad de code: "))
            changedguess = guess.copy()
            j = 0
            for c in guess:
                if c == code[j]:
                    pins.append("BLACK")
                    changedcode.remove(c)
                    changedguess.remove(c)
                j += 1
            for d in changedguess:
                if d in changedcode:
                    pins.append("WHITE")
                    changedcode.remove(d)
            pins.sort()
            print(pins)
            if pins == ["BLACK", "BLACK", "BLACK", "BLACK"]:
                print("Gefeliciteerd! Je hebt de code geraden")
                geraden = True  #Zorgt er voor dat de "Helaas" line niet geprint wordt
                break
            pins = []
        if geraden == False:
            print("Helaas, je gokken zijn op!")
    else:
        code = spel
        geraden = False
        possCombs = createPossibleCodes(["R", "O", "G", "Y", "P", "B"], 4)
        guesses = 1
        while geraden == False:
            nextGuess = list(pickGuess(possCombs))
            possCombs.remove(nextGuess)
            answer = codeControleren(code, nextGuess)
            if len(answer) == 0:                        #Deze if-statement zorgt ervoor dat als de laatste guess 0 kleuren goed had, deze kleuren niet meer worden gebruikt
                colorsNotInAnswer = []
                for letter in nextGuess:
                    if letter not in colorsNotInAnswer:
                        colorsNotInAnswer.append(letter)
                for color in colorsNotInAnswer:
                    for comb in possCombs:
                        if color in comb:
                            possCombs.remove(comb)
            if answer != "done" and len(answer) == 4:   #Deze if-statement zorgt ervoor dat als je 4 pins hebt, en dus alle kleuren weet de bot alleen nog opties probeert met die kleuren
                colorsInCode = []
                for letter in nextGuess:
                    if letter not in colorsInCode:
                        colorsInCode.append(letter)
                colorsNotInCode = ["R", "O", "Y", "G", "B", "P"]
                for color in colorsInCode:
                    colorsNotInCode.remove(color)
                for color in colorsNotInCode:
                    for comb in possCombs:
                        if color in comb:
                            possCombs.remove(comb)

            if answer == "done":
                geraden = True
                print("De bot heeft het geraden in " + str(guesses) + " gokken")
            guesses += 1

#spelkiezen()
#codezetten()
mainfunc()











