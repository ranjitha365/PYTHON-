# creating dictionary from user input (name and marks)
student = {}  # empty dict

name = input("Eneter your name:")   # taking input by user
marks = input("Enter your marks:")

student["name"] = name              #accessing dictionary
student["marks"] = marks

print("student information:", student) # get ready to output