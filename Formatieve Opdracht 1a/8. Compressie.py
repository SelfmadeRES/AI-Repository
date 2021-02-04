"""Opdracht 8 - Compressie
Schrijf een compress-programma, dat uit een gegeven bestand een nieuwe bestand maakt, waarbij van iedere regel alle spaties en tabs aan het begin van de regel zijn verwijderd.
Verder zijn alle lege regels verwijderd (een lege regel bevat ’\n’ , eventueel voorafgegaan door spaties en tabs(‘\t’))."""

from shutil import copyfile

file = open("sample.txt", "w")
file.write("Hello world\nI am learning python\n\nThis is a hard exercise\n\tBut im hanging in there.")
file.close()

def compress():
    copyfile("sample.txt", "compressed.txt")
    with open("compressed.txt", "r") as f:
        lines = f.readlines()
    with open("compressed.txt", "w") as f:
        for line in lines:
            line = line.replace(" ", "")
            line = line.replace("\n", "")
            line = line.replace("\t", "")
            print(line)
            f.write(line)
    f.close()

compress()



