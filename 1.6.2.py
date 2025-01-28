
Calculator = []
while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Break")

    MenuChoice=input(":")


    if MenuChoice=="1":
        try:
            Addition1=int (input("Whats the first number do you want to use:"))
            Addition2=int (input("Whats the second number do you want to use:"))
            print("The number is",(Addition1)+(Addition2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice=="2":
        try:
            Subtraction1=int (input("Whats the first number do you want to use:"))
            Subtraction2=int (input("Whats the second number do you want to use:"))
            print("The number is",(Subtraction1)-(Subtraction2))
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    elif MenuChoice=="3":
        try:
            Multiplication1=int (input("Whats the first number do you want to use:"))
            Multiplication2=int (input("Whats the second number do you want to use:"))
            print("The number is",(Multiplication1)*(Multiplication2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice=="4":
        try:
            Division1=int (input("Whats the first number do you want to use:"))
            Division2=int (input("Whats the second number do you want to use:"))
            print("The number is",(Division1)/(Division2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice=="5":
        break
    else:
        print("You sir, didn't use the right choice. Do better!")
    