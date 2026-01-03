# GETTERS (it is said to ba an a output)

class person:
    def __init__(self):
        self.__age = 19

    def get_age(self):
        return self.__age
    
p = person()
print(p.get_age())


# setters (it may update the value)

class person:
    def __init__(self):
        self.__age = 19

    def get_age(self):
        return self.__age
    
    def set_age(self,value):
        self.__age = value
    
p = person()
p.set_age(25)
print(p.get_age())
