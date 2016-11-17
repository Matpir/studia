


a=set([1,2,3])
b=frozenset([2,3,4])



#klucze w slownikach
slownik = {b:9}
print slownik

#elementy innych zbiorow
c=set([5,4,9])
c.add(b)
print c

#zbior pusty
d=set()
print d

#operacje na zbiorah

#licba elementow
print len(a), len(b), len(c), len(d)

#sprawdzamy czy dany obiekt jest elementem zbioru
print 5 in a, 5 in b, 5 in c, 5 in d

#sprawdzamy czy dany obiekt nie jest elementem zbioru
print 8 not in a, 8 not in b, 8 not in c, 8 not in d
print'\n'

#sprawdzanie czy dany zbior jest podzbiorem innego zbioru
print set([1,2]) <= a
print set([3,4]) <= b
print set([1]) <= b
print set([1,3,5]) <= a

print a.issubset(b)
print'\n'

#sprawdzanie czy dany zbior jest nadzbiorem danego zbioru
print a>=set([1,2])
print b>=set([3,4])


print a.issuperset(b)
print '\n'

#laczneie zbiorow
e=a | b
print e
print '\n'

#czescwspolna dwoch zbiorow
f=a&b
print f
print '\n'

#roznica 2 zbiorow
print a-b
print b-a
print '\n'

#roznica symetryczna
g=a^b
print g






