#mastermind
#imports
import random




def spelkiezen():  #Deze functie laat de speler kiezen of hij wil raden of zetten. Als hij voor zetten kiest moet hij een code in formaat "CODE" kiezen
    spelsoort = input("Wil je raden of zetten: ")
    if spelsoort == "raden":
        return spelsoort
    elif spelsoort == "zetten":
        code = input("Wat is je code (R, O, Y, G, B, P): ")  #De toegestane kleuren zijn Red, Orange, Yellow, Green, BLue en Purple
        return code

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
    gok = []
    if beurt == 1:
        for i in range(2):
            gokletter = random.choice(lettersleft)
            gok.append(gokletter)
            gok.append(gokletter)
            lettersleft.remove(gokletter)
    elif feedback == [] and beurt == 2:
        for i in range(2):
            gokletter = random.choice(letters)
            gok.append(gokletter)
            gok.append(gokletter)
            lettersleft.remove(gokletter)
    elif feedback == [] and beurt == 3:
        for i in range(2):
            gokletter = random.choice(letters)
            gok.append(gokletter)
            gok.append(gokletter)
    
    return gok
    #print(gok, [])

raadbot(1)
def mainfunc():
    spel = spelkiezen()
    geraden = False
    if spel == "raden":
        code = codezetten() #De code wordt de code die random is gekozen
        pins = []   #Hier komen de pins die het antwoord geven
        #print(code)
        for i in range(1, 13):
            print("Gok " + str(i) + ":")
            guess = list(input("Raad de code: "))
            for j in range(4):
                if guess[j] == code[j]:
                    pins.append("BLACK")
                elif guess[j] in code:
                    pins.append("WHITE")
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

#spelkiezen()
#codezetten()
#mainfunc()











print("""________________________
|------C  O  D  E------|
|----------------------|
|12**--_  _  _  _------|
|--**------------------|
|----------------------|
|11**--_  _  _  _------|
|--**------------------|
|----------------------|
|10**--_  _  _  _------|
|--**------------------|
|----------------------|
|9-**--_  _  _  _------|
|--**------------------|
|----------------------|
|8-**--_  _  _  _------|
|--**------------------|
|----------------------|
|7-**--_  _  _  _------|
|--**------------------|
|----------------------|
|6-**--_  _  _  _------|
|--**------------------|
|----------------------|
|5-**--_  _  _  _------|
|--**------------------|
|----------------------|
|4-**--_  _  _  _------|
|--**------------------|
|----------------------|
|3-**--_  _  _  _------|
|--**------------------|
|----------------------|
|2-**--_  _  _  _------|
|--**------------------|
|----------------------|
|1-**--_  _  _  _------|
|--**------------------|
|----------------------|""")