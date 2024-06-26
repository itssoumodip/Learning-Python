"""
factorial(5) = 5*4*3*2*1
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1
factorial(0) = 1 # BY DEFAULT
"""
def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter the NO. : "))
print("Factorial of", n,"is : ", factorial(n))

# factorial (5)
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = 120