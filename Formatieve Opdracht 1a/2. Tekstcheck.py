"""Opdracht 2 - Tekstcheck
Schrijf een functie die de eerste index teruggeeft waarop twee strings een verschillende waarde hebben.
Bedenk zelf een goede functienaam. Het complete programma vraagt om twee strings aan de gebruiker en print de index waarop deze twee strings verschillen.
Zorg je dat de functie goed test. Let op: een string mag spaties bevatten!"""

def stringComparison(string1, string2):
    for i in string1:
        string1index = string1.index(i)
        if i != string2[string1index]:
            return string1.index(i)


stringComparison("Ik houd van taco's", "Ik houd niet van hamburgers")