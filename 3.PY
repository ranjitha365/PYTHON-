class Animal:
    def make_sound(self):
        super().make.sound()
        print(f"{self.name} is barking")

    def get_angry(self):
        print("animal is barking")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print ("cat is meowing")
    def get_angry(self):
        super().get_angry()
        print("the cat hisses!")


        


    D = Cat()
    D.make_sound()
    D.gey_angry()









        







  