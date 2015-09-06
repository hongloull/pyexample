class Person(object):

    def __init__(self, name):
        self._name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    def __init__(self,name):
        super(SubPerson,self).__init__(name)

    @Person.name.getter
    def name(self):
        print('SubPerson get name')
        return super(SubPerson,self).name

    @name.setter
    def name(self, value):
        print('SubPerson set name.')
        super(SubPerson, SubPerson).name.__set__(self, value)

p = SubPerson('foo')
p.name = 'tom'
print(p.name)
