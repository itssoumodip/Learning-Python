#Default Arguement 
def multiplication(a=1, b=2):
    print(a,"x",b,"=",a*b)

multiplication()
multiplication(2,2)   # this is
multiplication(3,2)
multiplication(4)
multiplication(b=5)

# Keyword argument
multiplication(b=4, a=5)

# Keyword Arbitrary Arguments
def average (*number):
    sum = 0 
    for i in number:
        sum = sum+i
    print("Average : ", sum/len(number))
average(5, 6)

## Function with Calling 
def average_2 (*number_2):
    sum_2 = 0 
    for i in number_2:
        sum_2= sum_2+i
    return sum_2/len(number_2)

return_value = average_2(3,3,3,3,3,3,3)
print(return_value)