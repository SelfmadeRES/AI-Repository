"""Opdracht 12 - FizzBuzz
Schrijf een programma dat de getallen 1 tot 100 print, maar print voor veelvouden van drie “fizz” in plaats van het getal en voor veelvouden van vijf print “buzz” in plaats van
het getal. Getallen die zowel veelvoud zijn van drie als van vijf worden afgedrukt als “fizzbuzz"""

def FizzBuzz():
    x = range(1, 101)
    for n in x:
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

FizzBuzz()
