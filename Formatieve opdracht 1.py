"""Opdracht 1
Schrijf een programma dat een piramide van variabele lengte indrukt, zoals in het voorbeeld. Druk ieder character
apart af. De gebruiker geeft aan hoe groot de piramide is. Implementeer je programma twee keer, de eerste keer met
twee for loops, en daarna met twee while loops. Maak ook versies die de pyramide een andere kant op laten wijzen."""

def forLoopPyramid(teken):
    grootte = int(input("Hoe groot?"))
    for i in (2 * grootte - 1):
        for j in abs(grootte - i):
            print(teken)
        print("\n")
        
forLoopPyramid("*")
            
            
    