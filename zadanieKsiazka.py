# napisz skrypt, ktora dziala jak ksiazka adresowa:
# dane powinno dac sie wprowadzic, usunac i zmodyfikowac
# dane powinny byc wyswietlane w postaci tabelki
# dodaj unikatowy numer (np PESEL)

from prettytable import PrettyTable

peopleList = []
tablePersonalData = PrettyTable(
    ['Imie', 'Nazwisko', 'PESEL', 'Tel.', 'Miasto', 'Kod pocztowy', 'Ulica', 'Nr domu / mieszkania.'])


class Person(object):
    def __init__(self, name, surname, pesel, tel, address):
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.tel = tel
        self.address = address


class Address(object):
    def __init__(self, street, buildingNumber, postalCode, cityOrTown):
        self.street = street
        self.buildingNumber = buildingNumber
        self.postalCode = postalCode
        self.cityOrTown = cityOrTown


def isPeopleListEmpty():
    if (peopleList.__len__() == 0):
        return True
    else:
        return False


def addPersonToDisplay(person, forcePrint):
    tablePersonalData.add_row(
        [person.name, person.surname, str(person.pesel), str(person.tel), person.address.cityOrTown,
         person.address.postalCode, person.address.street, person.address.nr])
    if (forcePrint):
        print tablePersonalData


def displayAllPeople():
    i = 0
    while i < peopleList.__len__():
        person = peopleList[i]
        addPersonToDisplay(person, False)
        i += 1
    print tablePersonalData


def searchPerson(pesel):
    i = 0
    personFound = False
    while i < peopleList.__len__():
        if (peopleList[i].pesel == pesel):
            personFound = True
            break
        i += 1
    if (personFound):
        return i
    else:
        return None


def addPerson():
    person = Person("", "", "", "", "")
    address = Address("", "", "", "")

    print "PESEL: "
    person.pesel = input()
    searchResult = searchPerson(person.pesel)
    if (searchResult is not None):
        print "Ta osoba juz istnieje w bazie!"
        return

    print "Imie: "
    person.name = raw_input()
    print "Nazwisko: "
    person.surname = raw_input()
    print "Numer tel: "
    person.tel = raw_input()
    print "Miasto zamieszkania: "
    address.cityOrTown = raw_input()
    print "Kod pocztowy: "
    address.postalCode = raw_input()
    print "Ulica: "
    address.street = raw_input()
    print "Nr domu / mieszkania: "
    address.nr = raw_input()
    person.address = address
    peopleList.append(person)
    print "Dodano pomyslnie!"


def deletePerson(pesel):
    searchResult = searchPerson(pesel)

    if (searchResult is not None):
        peopleList.__delitem__(searchResult)
        print "Usunieto czlowieka!"
    else:
        print "Nie znaleziono czlowieka o podanym numerze PESEL."


def menu():
    while (1):
        tablePersonalData.clear_rows()
        print "_____________________________"
        print "MENU"
        print "1: Dodaj osobe\n2: Wyszukaj\n3: Wyswietl wszystkie osoby\n4: Usun\n"

        print "Podaj nr operacji: "
        operacja = input()
        if (operacja > 1):
            if (isPeopleListEmpty()):
                print "Ksiazka adresowa jest pusta."
                menu()
                return

        if (operacja == 1):
            addPerson()
        elif (operacja == 2):
            print "Podaj PESEL osoby do wyswietlenia: "
            pesel = input()
            searchResult = searchPerson(pesel)
            if (searchResult is not None):
                addPersonToDisplay(peopleList[searchResult], True)
            else:
                print "Nie znaleziono czlowieka o podanym numerze PESEL."
        elif (operacja == 3):
            displayAllPeople()
        elif (operacja == 4):
            print "Podaj PESEL osoby do usuniecia: "
            pesel = input()
            deletePerson(pesel)
        else:
            print "Nie znaleziono operacji."


menu()
