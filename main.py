#PROGRAMMING ASSIGNMENT #1 - Number/Word Parser
#CMSC128 AB-3L, 2013-32091
#REFERENCES
# BASIC numToWord function - http://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-in-python

def numParseTens(number_in):
    #Defined Dictionary and List of number strings
    ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    tens1 = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    #For parsing numbers 1-99
    if(number_in < 11):
        return (ones[number_in])
    elif(number_in > 10) and (number_in < 20):
        return (tens1[number_in])
    elif(number_in > 19) and (number_in < 100):
        tens_place, ones_place = divmod(number_in, 10)
        if(ones_place == 0):
            return(tens2[tens_place-2])
        else:
            return(tens2[tens_place-2] + '-' + ones[ones_place])
        
def numParseHundreds(number_in):
    #For parsing 100-1000
    hundreds_place, rem_number = divmod(number_in, 100)
    if(rem_number == 0):
        return(numParseTens(hundreds_place) + ' hundred')
    else:
        return(numParseTens(hundreds_place) + ' hundred ' + numParseTens(rem_number))

def numParseThousands(number_in):
    #For parsing 1000-999999
    thousands_place, rem_number = divmod(number_in, 1000)
    if(rem_number == 0):
        if(thousands_place < 100):
            return(numParseTens(thousands_place) + ' thousand')
        elif(thousands_place > 99) and (thousands_place < 1000):
            return(numParseHundreds(thousands_place) + ' thousand')
    else:
        if(thousands_place < 100):
            return(numParseTens(thousands_place) + ' thousand ' + numParseHundreds(rem_number))
        elif(thousands_place > 99) and (thousands_place < 1000):
            return(numParseHundreds(thousands_place) + ' thousand ' + numParseHundreds(rem_number))
    
def num2word(number_in):

    if(number_in == 0):
        #Parser for zero
        print("zero")
    elif(number_in != 0) and (number_in < 100):
        print(numParseTens(number_in))
    elif(number_in > 99) and (number_in < 1000):
        print(numParseHundreds(number_in))
    elif(number_in > 999) and (number_in < 1000000):
        print(numParseThousands(number_in))
    elif(number_in == 1000000):
        #Parser for one million
        print("one million")
    else:
        #Error Catching for out of range
        print("Input out of range!(0-1000000)")
    
        
def selectFunction(choice):
    #Function that routes to the function chosen
    firstArgument = input("Enter First Argument: ")

    if choice == 1:
        inputArg = eval(firstArgument)
        num2word(inputArg)
        
    elif choice == 2:
        print("Not Implemented Yet!")
        start()
        
    elif choice == 3:
        print("Not Implemented Yet!")
        start()
        
    elif choice ==  4:
        print("Not Implemented Yet!")
        start()
    elif choice ==  5:
        print("Good bye!")
    else:
        print("Wrong Input!")
        start()
        
def start():
    #Provides interface for the functions
    print("MENU:")
    print("1.numToWords")
    print("2.wordsToNum")
    print("3.wordsToCurrency")
    print("4.numberDelimited")
    print("5.Exit")
    choice = eval(input("Choice:"))
    selectFunction(choice)
