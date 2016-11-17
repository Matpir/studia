# skrypt, ktory losuje 6 niepowtarzajacych sie liczb od 1 do 35

import random

random.seed()

l = []

i = 0
while i < 6:
    losowa = l.append(random.randint(1, 35))
    if not l.__contains__(l.append(random.randint(1, 35))):
        l.append(random.randint(1, 35))
i+=1

print l
