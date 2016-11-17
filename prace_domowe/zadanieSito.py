print "Podaj koniec zakresu:"
calcTo = input()
calcTo += 1

notPrimeNumbers = []

for i in range(2, calcTo):
    if i not in notPrimeNumbers:
        print (i),

        for j in range(i * i, calcTo, i):
            notPrimeNumbers.append(j)
