#Opdracht 11 - Caesarcijfer
#Schrijf een programma voor Caesarcijfers.

def caesar():
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"     #lists met alle letters
    lowercases = "abcdefghijklmnopqrstuvwxyz"
    toChange = input("Geef een tekst: ")        #vragen om inputs
    n = eval(input("Geef een rotatie: "))
    changed = ""
    for char in toChange:
        if char in capitals:
            newLetter = capitals[(capitals.index(char) + n) % 26]       #bij hoofdletters veranderen in passende hoofdletter
            changed += newLetter
        elif char in lowercases:
            newLetter = lowercases[(lowercases.index(char) + n) % 26]   #bij kleine letters zelfde gebal
            changed += newLetter
        else:
            changed += char                 #leestekens veranderen niet
    return changed

print(caesar())

