# file handling

class Database:
    def __init__(self):
        self.storage = {}
    def write(self, key, value):
        self.storage[key] = value
    
    def read(self,key):
        if key in self.storage:
              
              print(self.storage[key])
        else:
            print("DB item not available")
db = Database()
db.write("name", "chandan")
db.read("chandan",)




