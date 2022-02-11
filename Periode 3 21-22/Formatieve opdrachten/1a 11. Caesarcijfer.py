#Opdracht 11 - Caesarcijfer
#Schrijf een programma voor Caesarcijfers.

def caesar():
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercases = "abcdefghijklmnopqrstuvwxyz"
    toChange = input("Geef een tekst: ")
    n = eval(input("Geef een rotatie: "))
    changed = ""
    for char in toChange:
        if char in capitals:
            newLetter = capitals[(capitals.index(char) + n) % 26]
            changed += newLetter
        elif char in lowercases:
            newLetter = lowercases[(lowercases.index(char) + n) % 26]
            changed += newLetter
        else:
            changed += char
    return changed

print(caesar())

