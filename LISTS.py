# lists
items = ["bru", "milk,wate,"]
print(items)
print(items[0]) # to get a perticular one species


d = ["s","e","r"]
print(d)
d.pop()   # for removing a last element
print(d)
d.append("mom's magic")
print(d)
d.remove("s")
print(d)
d.insert(1,"sugar") # insert used for which postion of that product we need so
print(d)

# list slicing
l = [100, 200, 300,]
print(l[1::3])
 
# sorted_lists
items = [55,1,29,68,8] # for getting a orderly of that product
print(sorted(items))
rev = items.reverse()
print(items)