# cmsc128-ay2015-16-assign001-py
A CMSC128 assignment, creating a functions that revolves in parsing numbers to words.

Functions:
* numToWords - Accepts a whole number from zero (0) to 1 million (1000000; without commas for example: 1,000,000) and prints on screen the number in word form.
* wordsToNum - Accepts a number in word form (from zero to 1 million) and returns it in numerical form. Input must be in lowercase.
* wordsToCurrency - Accepts two arguments: the first argument is the number in word form (from zero to 1 million) and the second argument is any of the following: JPY, PHP, USD. The function returns the number in words to its numerical form with a prefix of the currency.
* numDelimited - Accepts three arguments: the first is the number from zero to 1 miliion, the second is the delimiter to be used (single character only) and third, the number of jumps when the delimiter will appear (from right most going to left most digit).
 
Notes:
* To access interface, use start() function.
* Imported re (regex) library to use inside the functions
