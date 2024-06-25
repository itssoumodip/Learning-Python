

# def greet(fx): ##or you can greet(hello)()
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this Function")
#     return mfx

def greet(fx): ##or you can greet(hello)()
    def mfx(*args, **kwargs):   ## *args takes the agrument as a Tupple
        print("Good Morning")   ## **kwargs takes the agrument as a Dicnory
        fx(*args, **kwargs)
        print("Thanks for using this Function")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a+b)
    
hello()
add(1,2)