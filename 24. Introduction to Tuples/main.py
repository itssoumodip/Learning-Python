# For making a Tupple
tup = (1, 3, 4, 'green', True)
print(type(tup))
# For making 1 value tupple
tup_another = (1,)
print(type(tup_another))
print(tup[0])
print(tup[1])
print(tup[2])

if 3 in tup:
    print("Yes present broo")

tup_2 = tup[2:4]
print(tup_2)
print(tup)