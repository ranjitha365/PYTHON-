#list comphrension
l = [x for x in  range (1,16)]
print(l)

dl = [x**2 for x in l if x%2==0]
print(dl)