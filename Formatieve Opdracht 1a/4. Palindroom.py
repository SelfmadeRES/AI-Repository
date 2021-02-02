"""Opdracht 4 - Palindroom
Schrijf een functie die checkt of een woord een palindroom is. Schrijf een versie die gebruikt maakt van een bibliotheekfunctie die een string voor je omdraait.
Maak ook een versie waarbij jij zelf het omdraaien verzorgt. Probeer zo min mogelijk code te gebruiken."""

def palindromeCheck(x):
    x = list(x)
    reversed_x = x[::-1]
    for i in x:
        if i != reversed_x[x.index(i)]:
            return "Nee"
    return "Ja"

print(palindromeCheck("palindroom"))



