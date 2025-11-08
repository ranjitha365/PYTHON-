#FUNCTIONS 
def greet ():
    print("hello, good moorning")
greet()

# functions parameeter (which data will go)
def freind(boy,girl):  # positional parameeter
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} friend {girl}")
freind("Dhanush", "Ranjitha")

#key word parameeter
def human(boy,girl):
    print(f"{boy} and {girl} are human")
human(boy="dhanu",girl="ranjitha") # key word parameeter

#default parameeter
def celebraty(boy,girl="girl"): #if in case we dont know who's a girl so
    print(f"{boy} famoused celebraty{girl}")
celebraty(boy="allu arjun",)

#returning values from a functioN  # modifying code

def func(num):
    return int(str(num*5))

a = 100
b = func(2)
c = a + b
print(c)

#FUNCTIONS ADVANCE
#1 VARIABLE LENGTH ARGUEMENTS
# using args
def add (*a):
    print(a)
add(1,2,3,3)

# adding numbers
def func(*num):
    return sum(num)
a = (1,2,4)
b = (1,2,3)
c = sum(a) + sum(b)
print(c)

# lambda funvtions: (anonymus function)
add = lambda x,y : x + y
print(add(1,3))

# if we doule this number
double = lambda x, y: 2 *x *y # for multiplaication
double = lambda x, y: 2 *x +y  #foradding
print(double(1, 5))

students = [ 
    {"name" : "chandan", "marks" : 50},
    {"name":"dhanu", "marks" : 20},
]
students.sort(key = lambda x:x["marks"],)
print(students)

 # a function called itself : Recursion
def greet ():
    print("hello")
greet()

#Nested loop:
def calculate(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    print(add())
    print(sub())
    print(mul())
calculate(10,2)

    

