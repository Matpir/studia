'''
instrukcje warunkowe i petle
'''

a=6
b=5
if a<4:
    print a
elif a>4:
    print b
else:
    print 0

for x in range(-10,11):
    print "%+i" %x, # + znak przed liczba

print "\n"

for x in range(5,100,10):
    print "%3i%6o%5x" % (x,x,x) #wyrownanie od prawej

for x in range(5,100,10):
    print "%-3i%-6o%-5x" % (x,x,x) #wyrownanie od lewej(# wlasciwy prefiks)

for x in range(5,100,10):
        print "%3i %#04o %#04o" % (x,x,x) # 0 - pole przeznaczone na liczy bedzie wypelnione 0

a =[1,2,3,4,5,6]
while a :
    a=a[:len(a)-1]
    print a