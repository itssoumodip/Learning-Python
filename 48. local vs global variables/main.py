x = 4
print(x)

def hello():
    global x  #For changing the x to global
    x = 5     ## x convert to 5 (GLOBALY)
    print(f"The Local x is : {x}")
    print("Hello World !!")
print(f"The Global x is : {x}")
hello()
print(f"The Global x After Change is : {x}")