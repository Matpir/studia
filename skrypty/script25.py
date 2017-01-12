# utworzenie i otwarcie do zapisu pliku 'plik1.txt'
fl = open("plik1.txt", "wb")

# 3 podstawowe atrybuty obiektow plikowych

# name - nazwapliku
print fl.name

# mode - okresla tryb w jakim otwarto plik
print fl.mode

# closed - okresla czy plik jest zamkniety
print fl.closed

# metody do obslugipliku

# write - zapisuje do pliku napis
fl.write("Pierwszy plik")

# flush - zapisuje dane z bufora do pliku
# przydane w przypadku systemu Windows

# \n - nowa linia w pliku
fl.write("\nNowa linia")

# close - zapisuje dane z bufora do pliku i zamyka plik
fl.close()

# otwarcie pliku do modyfikacji
fl = open("plik1.txt", "r+b")

# read - odczytywanie z pliku napis
print fl.read()

# tell - podaje aktualna pozycje w pliku
print fl.tell()

# seek - ustawia pozycje w pliku na podana
fl.seek(0)

# nadpisanie zawartosci pliku
fl.write("Nowy poczatek")

# wczytanie fragmentu zawartosci pliku o okreslonej dlugosci
print fl.read(14)

# writelines - zapisuje do pliku sekwencje napisow
# (bez dodawania automatycznie separatorow)
fl.writelines(["\n3linia" "\n4 linia" "\n5 linia"])

# readlines - wczytuje z pliku sekwencje napisow
fl.seek(0)
print fl.readlines()

# truncate - skraca plik na podanej pozycji
fl.truncate(30)
fl.seek(0)
print fl.read()

# isatty - zwraca True jezeli plik jest dolaczony do urzadzenia terminalowego
print fl.isatty()

# przyklad strumienie sys.stdout i sys.stdin
import sys

print sys.stdout.isatty()

# przyklad przekierowania wewnatrz programu
import sys

ekran = sys.stdout
sys.stdout = open("wyjscie.txt", "w")
print "Jestem tutaj"
print "Gdzie Ty poszedles?"
sys.stdout = ekran
print open("wyjscie.txt", "r").read()
