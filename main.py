#PROGRAMMING ASSIGNMENT #1 - Number/Word Parser
#Irvin Kean Paulus T. Paderes
#CMSC128 AB-3L, 2013-32091
#REFERENCES
# BASIC numToWord function - http://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-in-python
# text2num in python - https://github.com/ghewgill/text2num/blob/master/text2num.py
# Adding character at certain index -http://stackoverflow.com/questions/5254445/add-string-in-a-certain-position-in-python
import re

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
    #Converts number into its equivalent number words
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

def word2num(string_in):
    #Converts number words into its equivalent number
    small_numbers = {'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,
    'eleven': 11,'twelve': 12,'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18,'nineteen': 19,
    'twenty': 20,'thirty': 30,'forty': 40,'fifty': 50,'sixty': 60,'seventy': 70,'eighty': 80,'ninety': 90}
    try:
        if(string_in == 'zero'):
            #Parser for zero
            return(0)
        elif(string_in == 'one million'):
            #Parser for one million
            return(1000000)
        else:
            string_list = re.split(r"[\s-]+", string_in) #Regex that splits the string with delimiters space and '-'
            ret_int = 0
            curr_hndrd = 0
            for num in string_list:
                curr = small_numbers.get(num, None)
                if curr is not None:
                    curr_hndrd += curr
                elif(num == "hundred") and (curr_hndrd != 0):
                    curr_hndrd *= 100
                else:
                    if(num == "thousand"):
                        ret_int += curr_hndrd * 1000
                        curr_hndrd = 0
                    else:
                        #Error Catching for out of range
                        raise NameError('errInput')
            return(ret_int + curr_hndrd)
    except NameError:
        return("Wrong Input!")
        
def word2curr(string_in, currency):
    #Converts a number word into a currency
    return(currency + str(word2num(string_in)))

def numDelimited(string_in, char_delimiter, num_of_places):
    #Delimits the string with the given character by its places
    print(string_in[:-num_of_places] + char_delimiter + string_in[-num_of_places:])

def selectFunction(choice):
    #Function that routes to the function chosen
    if choice == 5:
        print("Good bye!")
    else:
        firstArgument = input("Enter First Argument: ")

        if choice == 1:
            try:
                inputArg = eval(firstArgument)
                num2word(inputArg)
            except NameError:
                print("Wrong Input!")
                start()
        elif choice == 2:
            output = word2num(firstArgument)
            if(output == "Wrong Input!"):
                print(output)
                start()
            else:
                print(output)

        elif choice == 3:
            currency_list = ['JPY', 'PHP', 'USD']
            secondArgument = input("Enter Currency: ")
            if(len(secondArgument) > 3):
                print("Not a valid Currency!")
                start()
            else:
                if(secondArgument in currency_list != None):
                    print(word2curr(firstArgument, secondArgument))
                else:
                    print("Currency not in supported list!")
                    start()
        elif choice ==  4:
            secondArgument = input("Enter delimiter character: ")
            if(len(secondArgument) > 1):
                print("Only characters are allowed to be delimiters!")
                start()
            else:
                thirdArgument = eval(input("Enter length: "))
                if (thirdArgument > 7):
                    print("Length exceeds the length of the first argument!")
                    start()
                else:
                    numDelimited(firstArgument, secondArgument, thirdArgument)
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
