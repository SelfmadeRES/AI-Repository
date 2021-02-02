"""Opdracht 3 - Lijstcheck
a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.

b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.

c. Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
  - Het aantal enen is groter dan aan het aantal nullen
  - Er mogen niet meer dan 12 nullen zijn.
Bedenk zelf wat het return type van deze functie moet zijn. Gebruik in je programma de functie count() die je hebt geschreven bij de vorige opgave."""

#a.

def count(x, list):
    currentCount = 0
    for i in list:
        if i == x:
            currentCount += 1
    return currentCount

#print(count(3, [4, 5, 7, 21, 3, 3, "nee", 3.1]))

#b.

def diffCheck(list):
    currentDiff = 0
    for i in list:
        if list.index(i) > 0:
            if abs(i - list[list.index(i)-1]) > currentDiff:
                currentDiff = abs(i - list[list.index(i)-1])
    return currentDiff



#print(diffCheck([2, 4, 12, 8, 11]))

#c.

def count2(list):
    currentCountZeros = 0
    currentCountOnes = 0
    for i in list:
        if i == 0:
            currentCountZeros += 1
        elif i == 1:
            currentCountOnes += 1
    if currentCountOnes > currentCountZeros:
        return True
    else:
        return False

#print(count2([1, 1, 2, 0, 1, 0, 0, 0, 1, 0, 1, 2]))

