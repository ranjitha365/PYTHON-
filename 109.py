from functools import reduce

scores = [45,67,89,34,76,90]

# 1 increase all scores by using map

updated = list(map(lambda X : X + 5, scores))

# filter only passing students (>=50)

passed = list(filter(lambda x : x >= 50, updated))

# find the total marks of all passed students using reduce 
total = reduce(lambda x,y : x+ y, passed)

print("updated scores:",updated)
print("updated students:", passed)
print("Total marks:", total)



# ITERATORS AND GENERATORS

nums = [1234,457,897]

for num in nums:
    print(num)

it = iter(nums)

print(next(it))


class countDown:
    def __init__(self,start) :
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0 :
           raise  StopIteration
        num = self.start <= 0 
        self.start -= 1
        return num
cd = countDown(5)

for i in cd:
    print(i)


# all generators are iterstor

# to create an iterators generator is one better approach

# generartors in python 

# writing iterators manually can be complex

# A python provides generators to make this easy 
# a generator is a function that that uses the keyboard yeild instead of return


def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))


def simple_gen(x):
    for i in range(x):
        yield i

g = simple_gen(6)

c = 0
for i in g:
    c >=2

    break
    print(i)

    c += 1
    

#GENERATORS EXPRESSION

l = [x*x for x in range(1,101)]
print(type(l))                           # if use this at once it waas stay in memory

gl = (x*x for x in range(1,101))
print(type(gl))                          # but in this case didn't stay in memory


# to get an size of the generators code do it inn this form of code

import sys
l = [x*x for x in range(1,101)]
print(type(l))
print(sys.getsizeof(l))

gl = (x*x for x in range(1,101))
print(type(gl))
print(sys.getsizeof(gl)) # it was used in large data processing like files,solgs,streaming data















