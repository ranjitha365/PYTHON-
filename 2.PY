
# MATH CASE IN PYTHON

# match case
num = int(input("num:"))
match num :
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _:
        print("some other number")
        

Day = "sunday"

match Day:
    case "Monday":
        print("start of the work week")
    case "Friday":
        print("Alomost weekend")
    case "saturday" | "sunday":
        print("It's weekend!")
    case _:
        print("Just another weekday.")


time = 17
is_hungry = True

match time :
    case 9:
        print("Breakfast")
    case 14 | 13:
        print("lunch")
    case 17 if is_hungry:
        print("snacks")
    case 20:
        print("Dinner")
    case _: 
        print("work")


# Decoraters in python 
#Behaviour of a function without changing its actual code.

# why we use decorator 

# to add extra functionality to existing functions 
# used in logging timing access control
#helps write clean and reusable code 

# Decorater syntax

def decorater_name(func):
    def wrapper():
        print("Namaskara")
        func()
        print("Take care:")
    return wrapper
@decorater_name
def intro():
    print("iam chandan from karnataka")
intro()

@decorater_name
def bye():
    print("bye")
bye()


















    



