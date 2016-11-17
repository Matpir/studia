class Adres:
    pass

adr1 = Adres()
adr1.ulica = "Stonogi"
adr1.nr = 23
adr1.kod = "64-345"
adr1.miasto = "Dno"

print adr1.ulica
print adr1.__dict__