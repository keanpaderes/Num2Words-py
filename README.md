# cmsc128-ay2015-16-assign001-py
A CMSC128 assignment, creating a functions that revolves in parsing numbers to words.

## Introduction
One of the most popular job test for most software companies is the convertion of numbers into word form and vice versa. This assignment is to train CMSC 128 students for job interviews and to learn/master languages that students can use.

<i><em>URL to the project specification</em> - [https://goo.gl/UZs11p](https://goo.gl/UZs11p)</i>

## Instructions
- **Use of CL Interface** - I've included a CLI for this function library. To access interface, use the start() function after importing it.
- **Import of the library** - Each functions can be used by themselves as long as the proper parameters is included. Just import it normally in Python.

## Functions
- **void numToWords** - Accepts a whole number from zero (0) to 1 million (1000000; without commas for example: 1,000,000) and prints on screen the number in word form.
- **void wordsToNum** - Accepts a number in word form (from zero to 1 million) and returns it in numerical form. Input must be in lowercase.
- **void wordsToCurrency** - Accepts two arguments: the first argument is the number in word form (from zero to 1 million) and the second argument is any of the following: JPY, PHP, USD. The function returns the number in words to its numerical form with a prefix of the currency.
- **void numDelimited** - Accepts three arguments: the first is the number from zero to 1 miliion, the second is the delimiter to be used (single character only) and third, the number of jumps when the delimiter will appear (from right most going to left most digit).
