



























class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, o):
        return self.a+o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("ForGeeks")
print(ob1+ob2)
print(ob3+ob4)
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))
print(A.__add__(ob1, ob2))
print(A.__add__(ob3, ob4))

