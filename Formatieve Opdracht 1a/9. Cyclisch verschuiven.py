"""Opdracht 9 - Cyclisch verschuiven
Schrijf een functie met twee parameters. De eerste parameter, ch, is een character. De tweede parameter, n, geeft aan hoeveel posities de bitjes van ch opgeschoven moeten
worden. Als n > 0 is dan worden de bitjes naar links geschoven. Als n < 0 is dan worden de bitjes naar rechts geschoven. De bitjes die wegvallen worden aan de andere kant van
de byte weer teruggeplaatst.
Voorbeeld 1: ch met bitwaarde 1011000 en n is gelijk aan 3 resulteert in een ch met de bitwaarde: 1000101.
Voorbeeld 2: ch met bitwaarde 1011100 en n is gelijk aan -4 resulteert in een ch met de bitwaarde: 1100101."""
import binascii

def shift(ch, n):
    an_array = bytearray(ch, "utf8")
    for byte in an_array:
        binary = bin(byte)
        print(binary)
        onlybinary = binary[2:]
        print(onlybinary)
    i = 0
    if n > 0:
        while i < n:
            onlybinary = onlybinary[1:] + onlybinary[0]
            i += 1
    elif n < 0:
        while i > n:
            onlybinary = onlybinary[len(onlybinary)-1] + onlybinary[:len(onlybinary)-1]
            i -= 1
    print(onlybinary)


shift("a", -4)
