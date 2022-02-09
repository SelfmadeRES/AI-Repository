#Opdracht 4 - Palindroom
#Schrijf een functie die checkt of een woord een palindroom is.
#Schrijf een versie die gebruikt maakt van een bibliotheekfunctie die een string voor je omdraait.
#Maak ook een versie waarbij jij zelf het omdraaien verzorgt. Probeer zo min mogelijk code te gebruiken.

def palindromeCheck(word):
    palindrome = True                   #variabele aanmaken
    word = word.lower()                 #zorgt ervoor dat hoofdletters niet uitmaken
    for i in range(len(word)):
        if word[i] != word[-i - 1]:     #vergelijkt elk teken met het gespiegelde teken aan de andere kant van het woord
            palindrome = False          #als het niet klopt voor de variabele op False gezet
    return palindrome

print(palindromeCheck("Racecar"))
