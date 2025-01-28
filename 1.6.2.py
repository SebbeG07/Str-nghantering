
Calculator = []
while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Break")

    MenuChoice=input(":")


    if MenuChoice=="1":
        Addition1=int (input("Whats the first number do you want to use:"))
        Addition2=int (input("Whats the second number do you want to use:"))
        print("The number is",(Addition1)+(Addition2))

    elif MenuChoice=="2":
        Subtraction1=int (input("Whats the first number do you want to use:"))
        Subtraction2=int (input("Whats the second number do you want to use:"))
        print("The number is",(Subtraction1)-(Subtraction2))

    elif MenuChoice=="3":
        Multiplication1=int (input("Whats the first number do you want to use:"))
        Multiplication2=int (input("Whats the second number do you want to use:"))
        print("The number is",(Multiplication1)*(Multiplication2))

    elif MenuChoice=="4":
        Division1=int (input("Whats the first number do you want to use:"))
        Division2=int (input("Whats the second number do you want to use:"))
        print("The number is",(Division1)/(Division2))

    elif MenuChoice=="5":
        break
    else:
        print("You sir, didn't use the right choice. Do better!")
    