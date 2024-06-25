# MAP FUNCTION SYNTAX - map(function, iterable)

def cube(x):
    return x**3

print(cube(2))
li = [1,2,3,4,5,6]
print("Original List : ", li)
# '''
# new_li = []
# for item in li:
#     new_li.append(cube(item))
# '''
new_li = list(map(cube,li))
print(new_li)

# FILTER - filter(predicate, iterable)
def filter_function(a):
    return a>4
new = list(filter(filter_function, li))
print(new)

# MAP FUNCTION USING LAMBDA -
lambda_use_map = list(map(lambda x: x**3, li))
print(lambda_use_map)

# USE REDUCE -
from functools import reduce
numbers = [1,2,3,4,5]
def mysum(x, y):
    return x+y
sum=reduce(mysum,numbers)
print(sum)
