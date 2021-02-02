"""Opdracht 5 - Sorteren
Bedenk en schrijf zelf een functie die een lijst met getallen op volgorde sorteert."""

def sortNumbers(list):
    lastnumber = list[0]
    for i in list:
        currentindex = list.index(i)
        if i < lastnumber:
            list[currentindex] = lastnumber
            list[currentindex - 1] = i
            sortNumbers(list)
        lastnumber = i

    return list

print(sortNumbers([20, 18, 41, 85, 7, 8
                   ]))