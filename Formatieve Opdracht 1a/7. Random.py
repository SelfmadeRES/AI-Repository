"""Opdracht 7 - Random
Schrijf een programma dat een willekeurig getal kiest en de gebruiker net zo lang laat gokken tot dat ze het goed hebben. """

import random

def randomGuess():
    getal = random.randint(1, 100)
    print(getal)
    guessed = False
    guess = int(input("Raad en getal tussen 1 en 100: "))
    if guess == getal:
        print("Goed geraden, het was " + str(getal))
        guessed = True
    while guessed == False:
        if guess != getal:
            guess = int(input("Helaas probeer nog een keer: "))
        else:
            print("Goed geraden, het was: " + str(getal))
            guessed = True

#randomGuess()