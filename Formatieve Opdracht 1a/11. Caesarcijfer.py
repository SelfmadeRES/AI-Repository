"""Opdracht 11 - Caesarcijfer
Schrijf een programma voor Caesarcijfers. Voorbeeld van de interactie met het programma:"""

def caesar():
    tekst = input("Geef een tekst: ")
    changed = ""
    rotatie = int(input("Geef een rotatie: "))
    charlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for char in tekst:
        if char in charlist:
            char = charlist[(charlist.index(char) + rotatie)]
            changed += char
            #print(char)
    return changed


print(caesar())
