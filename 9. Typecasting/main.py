'''
a = "1"
b = "2"
print(int(a)+int(b))  #TO CONVERT STRING TO INTEGER
'''
# Explicit Conversion V
string = "10"
no = 2
string_no = int(string) #thorow Error if the string is not a valid integer
sum = no + string_no
print("The sum of both numbers is :", sum)

# Implicit Conversion V #convert python compiler normaly
a = 2.1 
b = 2
print(a+b)
print(type(a+b))