#Opdracht 8 - Compressie
#Schrijf een compress-programma, dat uit een gegeven bestand een nieuwe bestand maakt,
#waarbij van iedere regel alle spaties en tabs aan het begin van de regel zijn verwijderd.
#Verder zijn alle lege regels verwijderd (een lege regel bevat ’\n’ , eventueel voorafgegaan door spaties en tabs(‘\t’)).

def compress():
    f = open("ToCompress.txt")
    f.readlines()
    f.close()
    for line in f:
        return

#Functie werkt nog niet