# a = (input("Enter the No. : "))
# print(f"Multiplication Table of {a} is : ")

# ## WE USE TRY KEYWORD TO CHEK THE ERROR IN THE LINE
# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as e:
#     print(e) ## For print the Error
#     print("Invalid Input !!") ## For print

# print("Some imp line")
# print("End of Program")

## FOR CHEKING VALUE ERROR
try: 
    num = int(input("Enter the Integer : "))
except ValueError:
    print("Invalid Input !! IT'S NOT A INTEGER")