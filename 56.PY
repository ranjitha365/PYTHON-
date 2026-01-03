# create a class called mobile.
#Attributes:
#brand 
#model
#price

#METHODS:
# apply__discount9()
# display details

# task to do :
#create two objects of mobile
# appy different discount
# display all details for both phones

class mobile :
    def __inite__(self,brand,model,price):
        self.brand = brand 
        self.model = model
        self.price = price

    def apply__discount(self,percent):
        discounted_price = self.price - (self.price * percent/100)
        return discounted_price

    def festival_offer(self,percent):
        new_price = self.apply_discount(percent)

        if new_price <= 3000 :
            return " dasara offer "
        else :
            return "deepavali offer"
        
s1 = mobile("vivo","pro",5000)
print("brand:", s1.brand)
print("model:", s1.model)
print("original price:",s1.price)

discount_percent = 20
new_price = s1.apply_discount(discount_percent)
print("price after discuont:",new_price)
print("offer type:",s1.festival_offer(discount_percent))


