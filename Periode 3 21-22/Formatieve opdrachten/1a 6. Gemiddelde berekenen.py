#Opdracht 6 - Gemiddelde berekenen
#Schrijf een functie die het gemiddelde van een lijst met cijfers berekent.
#Schrijf er ook een die als input een lijst van lijsten met cijfers krijgt, en als uitvoer een lijst met de gemiddelden teruggeeft.

def average(list):
    total = 0                       #total aanmaken
    for number in list:             #elk getal toevoegen aan total
        total += number
    average = total / len(list)     #delen door lengte van list
    return average

print(average([1, 2, 3, 4, 4, 5]))

def averageOfLists(lists):
    listTotal = []
    for list in lists:              #zelde idee als de functie hiervoor maar dan 2x in één
        total = 0
        for number in list:
            total += number
        averageOfList = total / len(list)
        listTotal.append(averageOfList)
        total = 0
    return listTotal

print(averageOfLists([[1, 2, 3], [2, 4, 6], [7, 8, 9]]))