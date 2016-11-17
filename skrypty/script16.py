'''
funkcje
'''

def pierw(n):
    return n**0.5

print pierw(3)

def pierw2(m):
    if m>=0 : return m**0.5

print pierw2(3)

def pierw3(m):
    if m>=0 : return m**0.5
    else: return (-m)**0.5*1j

print pierw3(-2)

def rs(a,b):
    return a-b,a+b

print rs(8,4)

def suma(*args):
    s=0
    for x in args:
        s+=x
    return s

print suma(*range(10))
print suma(1,2,3,4,5)

