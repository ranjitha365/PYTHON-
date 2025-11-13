# for removing duplicated dictionary
data = {'a':'1', 'b':'2', 'c':'1'}
unique = {}
for key, value in data.items():
    if list(data.values()).count(value) == 1:
        unique[key] = value
        print(unique)
    