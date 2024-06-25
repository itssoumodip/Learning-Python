questions = [
    [
        "What is the capital of India?", "Delhi", "Python", "French", "JavaScript", "Php", "None", 4
        ],
    [
        "Who is the first person to walk on the moon?", "Delhi", "Python", "French", "JavaScript", "Php", "None", 4
        ],
    [
        "What is the largest planet in our solar system?", "Delhi", "Python", "French", "JavaScript", "Php", "None", 4
        ],
    [
        "What is the smallest country in the world by area?", "Delhi", "Python", "French", "JavaScript", "Php", "None", 4
        ],
    [
        "What is the largest mammal in the world?", "Delhi", "Python", "French", "JavaScript", "Php", "None", 4
        ],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print()
    print(f"Qustion for Rs. {levels[i]}\n\n{question[i]}")
    print(f"a.{question[1]}\t\tb.{question[2]}")
    print(f"c.{question[3]}\td.{question[3]}")
    reply = int(input("Enter the Ans(1-4) or 0 to Quit : \n"))
    if (reply==0):
        money=levels[i-1]
        break
    elif (reply==question[-1]):
        print(f"Correct ans, you have won Rs. {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong Answer !!")
        break

print("Your Take Home Money : ", money)