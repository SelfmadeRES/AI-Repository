#Opdracht 5 - Sorteren
#Bedenk en schrijf zelf een functie die een lijst met getallen op volgorde sorteert.

def listSorter(list):
    sortedList = []                     #variabele voor gesorteerde list
    while len(list) > 0:
        sortedList.append(min(list))    #voeg kleinste waarde toe aan nieuwe list
        list.remove(min(list))          #verwijder die waarde dan uit de oude
    return sortedList

print(listSorter([3, 5, 4, 2, 4, 1]))


