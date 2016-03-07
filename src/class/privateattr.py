class Parent(object):
    def __init__(self):
        self.__name = 'parent name'

class Child(Parent):
    def __init__(self):
        super(Child,self).__init__()


p=Parent()
print(p._Parent__name)

c=Child()
print(c._Parent__name)

