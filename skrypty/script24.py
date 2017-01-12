'''
ffunkcje ulatwiajace przetwarzanie sekwencji
'''

# applay - wywolanie funkcji z parametrami
#uzyskamy z rozpakowaniej sekwencji
dziel = lambda x,y,z:(x+y)/z
print dziel(7,4,6)

xyz = (7,4,6)
print apply(dziel,xyz)

# map - wywoluje okreslona funkcje dla kazdego elementu sekwencji z osobna
print map(lambda x: x*x*x, range(10))
print map(dziel, range(10), range(10),[2]*10)

#zip - konsolidacja danych wartposci pojedynczego elementu listy wynikowej zalezy od wartosci pojedynczych elementow lis zrodlowych

print zip("abcdef", [1,2,3,4,5,6])
print zip(range(1,10), range(9,0,-1))
print zip("zip", range(0,9), zip(range(0,9)))

#funkcja filter sluzy do fiultrowania

#filtrowanie samoglosek
samogloska = lambda x: x.lower() in 'asddfg'
print samogloska('A')
print filter(samogloska, "Ala ma kota")

#filtrowanie innych znkopw
print filter(lambda x: not samogloska(x), "Ala ma kota")

#funkcja reduyce - agregowanie danbcy
#suma elementow
print reduce(lambda x,y: x+y, [1,2,3])

#suma kwadratow elementow
print reduce(lambda x,y: x+y, map(lambda x:x*x,range(1,3)))