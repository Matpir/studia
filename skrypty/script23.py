'''
wytwi\=orniki(list comp[rehensions
'''

l = range(1,21,2)
print l

#postac prosta

#podwojenie wartosci
print [2*x for x in l]

#para (x,kwadrat,x)
print [(x,x*x) for x in range(1,15)]

#tabela kodowa ascii
print [(x,ord(x)) for x in "ABCDEF"]

#lista zawietrajaca 10 ;pustych list
print [ [] for x in range(10)]


#POSTAC PROSTA WARUNKOWA

#licczby wieksze od 10
print [x for x in l if x>10]

#liczby podzielne przez 3 lub  5
print [x for x in range(1,20) if not (x%3) or not (x%5)]

#tabela kodowa ascii dla samoglos\ek
print [(x, ord(x)) for x in "ABCDEF" if x in "AEIOUY"]

#POSTAC ROZESZONA

#poary kazdy z kazdym
print [(x,y) for x in range(1,5)
       for y in range(4,0,-1)]

#roznica miedzy wartoscia z pierwszej i druiej listy
print [x-y for x in range(1,5)
       for y in range(4,0,-1)]


#sklejanie napisu z trzechj list
print ['x'+y+'z' for x in [1,2]
       for y in ['A', 'B']
       for z in [0, 3]]

#postac rozrzeszona z jednym warunkiem
#lemenent jest mniejszy od drugiego
print [(x,y) for x in range(1,5)
       for y in range(4,0,-1)
       if x<y]

#para kazdy z kazdym jezeli suma mniejsza od 7
print [(x,y) for x in range(1,5)
       for y in range(4,0,-1)
       if x+y<7]

#para kazdy z kazdym pod warunkiem ze pierwszty jesty parzysty lub drugi nie[arzysty
print [(x,y) for x in range(1,5)
       for y in range(4,0,-1)
       if not (x%2) or y%2]

#postac rozrzeszona z wileloma warunkami

#para kazdy element z kazdym pod warunkiem ze pierwszy jest parzysty a drugi nieparzysty
print [(x,y) for x in range(1,5) if not (x%2)
       for y in range(6,2,-1) if y%2]






