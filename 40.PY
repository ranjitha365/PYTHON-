#basic structure of for loop
for i in range(1,11):
    print(i,end= " ")

l = ["blue", "green", "white"]
for colours in l :
    print(colours, "_" )

# by using enumerate
place = "majestic"
for address in place:
    for index, address in enumerate (place):
        print(f"{address} is in {index}th index")

