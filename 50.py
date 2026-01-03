# Magic method
# Initialisation and object creation method

class A:

    def __init__(self,X):
        self.X = X
obj = A(10)
print(obj.X)




# string representation method

class A:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return f"value is {self.x}"
    
obj = A(15)
print(obj)







    

