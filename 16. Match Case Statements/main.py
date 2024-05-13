x = int(input("Enter the Value of X : "))

match x: 
    case 0:
        print("The No is 0")
    case 5: 
        print("The No is 5")
    case _ if x==2:
        print("Hello Brother")
    case _ if x!=3: 
        print("Hello Kaka")
    case _: #DEFAULT
        print(x)