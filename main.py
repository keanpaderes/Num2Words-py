def selectFunction(choice):
    #Function that routes to the function chosen
    firstArgument = input("Enter First Argument: ")

    if choice == 1:
        print(firstArgument)
    elif choice == 2:
        print(firstArgument)
    elif choice == 3:
        print(firstArgument)
    else:
        print(firstArgument)
        
def start():
    #Provides interface for the functions
    print("MENU:")
    print("1.numToWords")
    print("2.wordsToNum")
    print("3.wordsToCurrency")
    print("4.numberDelimited")
    choice = eval(input("Choice:"))
    selectFunction(choice)
