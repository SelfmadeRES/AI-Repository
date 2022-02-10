#Opdracht 8 - Compressie
#Schrijf een compress-programma, dat uit een gegeven bestand een nieuwe bestand maakt,
#waarbij van iedere regel alle spaties en tabs aan het begin van de regel zijn verwijderd.
#Verder zijn alle lege regels verwijderd (een lege regel bevat ’\n’ , eventueel voorafgegaan door spaties en tabs(‘\t’)).

def compress():
    f = open("ToCompress.txt")
    f.readlines()
    f.close()
    done = False
    charIndex = 0
    lineIndex = 0
    while done == False:
        if f[lineIndex][charIndex] == "" or f[lineIndex][charIndex] == "\n" or f[lineIndex][charIndex] == "\t":
            #remove char from line
            charIndex += 1
        else:
            lineIndex += 1
            charIndex = 0
        if lineIndex == len(f):
            done = True
    return

#Functie werkt nog niet