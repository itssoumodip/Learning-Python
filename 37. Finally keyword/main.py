# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

def fine ():
    try:
        li = [1,2,3,4]
        l = int(input("Enter the Index : "))
        print(li[l])
        return 1
    except:
        print("Some Error Occured !!")
        return 0
    finally:    ## FINALY CODE ALWAYS WILL BE EXCUTED 
        print("I am alwas Excecuted")
x = fine()
print(x)