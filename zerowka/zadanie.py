class A:
    def met(self):
        print '1'

class B(A):
    def met(self):
        print '2'

class C(B,A):
    pass

t=C().met()
