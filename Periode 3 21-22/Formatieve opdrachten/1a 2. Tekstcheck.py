#Opdracht 2 - Tekstcheck

#Schrijf een functie die de eerste index teruggeeft waarop twee strings een verschillende waarde hebben.
#Bedenk zelf een goede functienaam.
#Het complete programma vraagt om twee strings aan de gebruiker en print de index waarop deze twee strings verschillen.
#Zorg je dat de functie goed test. Let op: een string mag spaties bevatten!

def similarity_check(s1, s2):
    for i in range(len(s1)):        #De loop gaat door tot het eind van de eerste string
        if s1[i] != s2[i]:          #Controle of de twee symbolen gelijk zijn op index i
            print(f"De strings verschillen op index {i + 1}!")
            return                  #return-functie beeïndigd functie zodat eind print niet gerund wordt
    print(f"De strings zijn identiek!")
    return

similarity_check("string1 lijkt op string2", "string2 lijkt op string 1")