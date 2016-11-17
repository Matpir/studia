# napisz skrypt, ktory dziala jak gra w zgadywanie liczby

import random

random.seed()

wylosowana = random.randint(0, 100)

print "Podaj ilosc prob: "
iloscProb = input()

print "Podaj liczbe: "
zgadywana = input()

i = 0
while i<iloscProb:
    if zgadywana > wylosowana:
        print "Twoja liczba jest wieksza od wylosowanej"
    elif (zgadywana == wylosowana):
        print "Zgadles!"
        break
    else:
        print "Twoja liczba jest mniejsza od wylosowanej"
        print "Podaj liczbe: "

    i+=1

print "Koniec"
