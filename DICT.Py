# creating dictionary
names = {
    "name" : "Ranjitha",
    "age" : "17",
    "habits" : "reading books"
}
print(names["age"])
print(names.get("name","not found"))
names["games"]  = "kabaddi"
print(names)
names["games"] = "chess"
print(names)
names.pop("games")
print(names)

#methods of dictionary
print(names.items())
print(names.keys())
print(names.values())

item1 = {
    "names" :"sugar",
    "weight" : 1,
    "price": 44.7
}

item2 = {
    "name" : "sugar",
    "weight" : 2,
    "price" : 88.0
            
}
items = [item1, item2, ]
print(f"total weight: {item1["weight"] + item2["weight"]}kg")
