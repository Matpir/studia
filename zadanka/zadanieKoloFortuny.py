import random


class Category(object):
    def __init__(self, name, keys):
        self.name = name
        self.keys = keys

    def getKeys(self):
        return self.keys


class FortuneCircle(object):
    points = range(-10, 11)

    def setCategories(self, categories):
        self.categories = categories

    def getRandomCategory(self):
        return random.choice(self.categories)


class FortuneFileManager(object):
    def __init__(self, fileName):
        self.file = open(fileName, "r+b")

    def getCategoriesFromFile(self):
        lines = self.file.readlines()
        categories = []
        i = 1
        while (i < 0):
            if (lines[i] == "</kategorie>"):
                break

            j = 0
            while (lines[i] != ":"):
                categoryName = lines[i]
                j += 1

            i += 1


print "Witaj w grze KOLO FORTUNY\n"
print "Podaj liczbe uczestnikow: "
usersQuantity = input()

fortuneCircle = FortuneCircle()
fortuneFileManager = FortuneFileManager('plik.txt')
fortuneFileManager.getCategoriesFromFile()



# i = 0
# while(i<usersQuantity):
