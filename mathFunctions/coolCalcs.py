## function to add two numbers together.
def addNumbers(number1, number2):
    '''
    provide two numbers, returns total
    '''
    return number1 + number2



## function to subtract two numbers.
def subtractNumbers(number1, number2):
    '''
    provide two numbers, returns number 1 - number2
    '''
    return number1 - number2

##function that gathers all files in a folder together
import glob
def gatherFiles (path)
    '''
    provide path as string with file pattern (e.g. *.csv)
    returns all target files in list
    '''

    return glob.glob(path)