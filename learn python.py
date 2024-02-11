print("The Quiz Game")
choice=input("Are you up for the quiz?(yes/no) ")
if (choice=="yes") : 
    print("Okay then, you're ready!")
    print("Number 1")
    c1=int(input("What's the answer for 5^2 - 2^2? "))
    if(c1==21):
        print("Good job! You've got it correct!")
    else:
        print("Too bad! Better luck next time! The answer is ",5**2-2**2,"!")
else:
    print("Try again next time!")
