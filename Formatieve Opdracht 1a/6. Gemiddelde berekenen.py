"""Opdracht 6 - Gemiddelde berekenen
Schrijf een functie die het gemiddelde van een lijst met cijfers berekent. Schrijf er ook een die als input een lijst van lijsten met cijfers krijgt, en als uitvoer een lijst met de gemiddelden teruggeeft."""

def averageFromList(list):
    count = 0
    for i in list:
        count += i
    average = count / len(list)
    return average

#print(averageFromList([1, 3, 5, 7, 9, 10]))

def averageFromLists(lists):
    averages = []
    for i in lists:
        count = 0
        for j in i:
            count += j
        average = count / len(i)
        averages.append(average)
    return averages

#print(averageFromLists([[1, 3, 5], [2, 4, 6], [1, 7, 13]]))
