# napisz skrypt, ktory dziala jak gra w zgadywanie liczby

import random

random.seed()

wylosowana = random.randint(0, 100)

print "Podaj ilosc prob: "
iloscProb = input()

i = 0
while i < iloscProb:
    print "Podaj liczbe: "
    zgadywana = input()
    if (zgadywana == wylosowana):
        print "Zgadles!"
        break
    elif zgadywana > wylosowana:
        print "Twoja liczba jest wieksza od wylosowanej"
    else:
        print "Twoja liczba jest mniejsza od wylosowanej"
    i += 1

print "Koniec"
