## Using else with for loop
for i in range (4):
    print(i)
    if i == 2:
        break
else:
    print("sorry no i")
print("----------")
## Using else with whlie loop
i=0
while i<7:
    print("iteration no {} in for loop".format(i+1))
    i = i + 1 
    # if i == 4:             ##If we dont break the loop then full loop will be printed also the else block will be printed
    #     break
else: 
    print("Block of else print")