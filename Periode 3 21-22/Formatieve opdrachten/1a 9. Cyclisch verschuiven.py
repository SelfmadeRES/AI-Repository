#Opdracht 9 - Cyclisch verschuiven
#Schrijf een functie met twee parameters. De eerste parameter, ch, is een character.
#De tweede parameter, n, geeft aan hoeveel posities de bitjes van ch opgeschoven moeten
#worden. Als n > 0 is dan worden de bitjes naar links geschoven.
#Als n < 0 is dan worden de bitjes naar rechts geschoven. De bitjes die wegvallen worden aan de andere kant van
#de byte weer teruggeplaatst.
#Voorbeeld 1: ch met bitwaarde 1011000 en n is gelijk aan 3 resulteert in een ch met de bitwaarde: 1000101.
#Voorbeeld 2: ch met bitwaarde 1011100 en n is gelijk aan -4 resulteert in een ch met de bitwaarde: 1100101.
import math

def cyclic(ch, n):
    asciiValue = ord(ch)                        #char omzetten in ascii-waarde
    binaryValue = str(format(asciiValue, "b"))  #ascii-waarde omzetten in binaire waarde
    print(binaryValue)
    while len(binaryValue) < 8:
        binaryValue = "0" + binaryValue         #binaire waarde 8 bits lang maken
    print(binaryValue)
    cycled = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i < len(binaryValue):                 #waarden in nieuwe list veranderen in character bits
        cycled[(i + n) % 8] = binaryValue[i]
        i += 1
    endByte = ""
    for bit in cycled:                          #bit list veranderen in string
        endByte += str(bit)
    return endByte

print(cyclic("R", 4))