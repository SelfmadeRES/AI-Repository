#Opdracht 3 - Lijstcheck
#a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.

def count(x, list):
    xCount = 0
    for char in list:
        if char == x:       #Is x gelijk aan het geïtereerde character
            xCount += 1
    return xCount
#b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.

def biggest_difference(list):
    for index in range(1, len(list)-1):         #loopt door de lijst heen
        print(abs(list[index] - list[index-1])) #print het verschil tussen de geindexde waarde en die met index - 1
    return

#c. Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
  #- Het aantal enen is groter dan aan het aantal nullen
  #- Er mogen niet meer dan 12 nullen zijn.
#Bedenk zelf wat het return type van deze functie moet zijn. Gebruik in je programma de functie count() die je hebt geschreven bij de vorige opgave.

def binary_check(list):
    zeroCount = 0
    oneCount = 0
    for number in list:
        if number == 0:         #Als het getal een 0 is, voeg toe aan zeroCount, anders is het een 1 en dus voeg je dan toe aan oneCount
            zeroCount += 1
        else:
            oneCount += 1
    return oneCount > zeroCount and zeroCount <= 12     #Condities worden gecheckt en de returnwaarde is een boolean


print(count(3, [1, 12, 3, 5, 45, 8, 3, 56, 3, 3, 1, 5, 3]))
(biggest_difference([1, 12, 3, 5, 45, 8, 3, 56, 3, 3, 1, 5, 3]))
print(binary_check([0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]))