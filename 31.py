# for loops
name = "ranjitha"
for letters in (name):
    print(letters)


# by using f string
name = "ranjitha"
for index, letters in enumerate(name):
    print(letters*(index+1))

# by using dictionarys
I = [1, 2, 3]
for index, num in enumerate (I):
    print(f"{num} is in {index}th index")
    if num == 3:
        break
    else:
        print("all printed")

#dictionary
d = { "name":"isha","age": 25,}
for key, values in d.items():
    print(key, " :", values)