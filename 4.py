file = open("notes.txt", "r")
contents  = file.read()       # to read a file
print(contents)               # to get an output
file.close()                  # closing for files

file = open("notes.txt", "r")
contents = file.readlines()  
 # to read multiple of lines                      # of the same file 
print(contents)
file.close() 


file = open("notes.txt", "w") # write a code
file.write("ranjirtha") # hey guys this is ranjitha
file.close() 




file = open("notes.txt", "a") # append means if we are forgetting to add something agan we can put
file.write("\n,yashi")
file.close()


# using a "with key word"
with open("notes.txt", "r") as f :
    print(f.read())





