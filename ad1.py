# nested loops 
for i in range (1,23):
    print(f"2x{i} = {2*i}") # this is for one table


# for multiple tables
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j} = {i*j}")


# for adding numbers by using nest loop

numbers = [12,56,78,0]
total = sum(numbers)
print("sum of numbers=",total)

# by adding 1by one numbers
l= [2,34,54,64,]
toal = 0
for num in l:
   
   print(total)
total = total + num
print(total)


l = [12,34,56]
dl = []
for num in l:
    dl.append(num*2)
    print(dl)
