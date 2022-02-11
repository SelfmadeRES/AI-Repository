#Opdracht 12 - FizzBuzz
#Schrijf een programma dat de getallen 1 tot 100 print,
#maar print voor veelvouden van drie “fizz” in plaats van het getal en voor veelvouden van vijf print “buzz” in plaats van
#het getal. Getallen die zowel veelvoud zijn van drie als van vijf worden afgedrukt als “fizzbuzz”

for i in range(1, 101):     #loop door de cijfer 1 t/m 100
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)