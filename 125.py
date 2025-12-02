class parent:
    def display(self):
        print("parent display")

class  child(parent):
    def display(self):
        super().display()
        print("child display")
c = child()
c.display()
        

