#Opdracht 7 - Random
#Schrijf een programma dat een willekeurig getal kiest en de gebruiker net zo lang laat gokken tot dat ze het goed hebben.
import random


def numberPick():
    toGuess = random.randint(1, 100)        #Kiest een integer tussen 1 en 100
    print(toGuess)
    guessed = False
    while guessed == False:                 #Zolang het niet is geraden, blijft de functie een nieuwe gok vragen
        guess = eval(input("Wat is het nummer: "))
        if guess == toGuess:                #Als het wordt geraden wordt de loop en daarna de functie beeïndigd
            guessed = True
            print("Je hebt het goed geraden")
        else:
            print("Dat is niet het goede nummer")
    return

numberPick()
