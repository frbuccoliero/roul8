import random 
import numpy as np


def spin():
    return(random.randint(0,36))

def isOdd(n):
    return 1 if n%2==1 else -1

def isEven(n):
    return 1 if n%2==0 else -1

def is1to18(n):
    return 1 if 1 <= n <= 18 else -1

def is19to36(n):
    return 1 if 19 <= n <= 36 else -1

def is1stRow(n):
    return 2 if 1 <= n <= 12 else -1

def is2ndRow(n):
    return 2 if 13 <= n <= 24 else -1

def is3rdRow(n):
    return 2 if 25 <= n <= 36 else -1

def is1stCol(n):
    return 2 if n%3==1 else -1

def is2ndCol(n):
    return 2 if n%3==2 else -1

def is3rdCol(n):
    return 2 if n%3==0 and n>0 else -1

def is1stSex(n):
    return 5 if 1 <= n <= 6 else -1 

def is2ndSex(n):
    return 5 if 7 <= n <= 12 else -1 

def is3rdSex(n):
    return 5 if 13 <= n <= 18 else -1 

def is4thSex(n):
    return 5 if 19 <= n <= 24 else -1 

def is5thSex(n):
    return 5 if 25 <= n <= 30 else -1 

def is6thSex(n):
    return 5 if 31 <= n <= 36 else -1 

def isRed(n):
    return 1 if n in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] else -1

def isBlack(n):
    return 1 if n in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35] else -1

def isInNumbers(n,numlist):
    return 36-len(numlist) if n in numlist else -1*len(numlist)

def isSplitBet(n,numlist):
    return 16 if n in numlist else -2

def numberToAnalyze(lastNumbers):
    numberToAnalyze = 0
    if len(lastNumbers) == 0:
        numberToAnalyze = spin()
    else:
        j=-1
        try:
            while lastNumbers[j] == 0:
                j-=1
            numberToAnalyze = lastNumbers[j]
        except IndexError:
            numberToAnalyze = spin()
    return numberToAnalyze

def masanielloLin(numberToAnalyze,budget,betSize,minbet,masTries):
    numbers = []
    if isRed(numberToAnalyze) > 0:
        budgetPreSpin = budget
        randomNumber = spin()
        numbers.append(randomNumber)
        budget += (isBlack(randomNumber) * minbet * betSize * pow(2,masTries))
        if budgetPreSpin <= budget:
            lastIsWin = True 
            masTries = 0
        else:
            masTries+=1
            lastIsWin = False
    else:
        budgetPreSpin = budget
        randomNumber = spin()
        numbers.append(randomNumber)
        budget += (isRed(randomNumber) * minbet * betSize * pow(2,masTries))
        if budgetPreSpin <= budget:
            lastIsWin = True 
            masTries = 0
        else:
            masTries+=1
            lastIsWin= False
    return numbers,budget,lastIsWin,masTries
    
def fibonacci(n):
    fib = [1,1]
    for _ in range(0,100):
        fib.append(fib[-1]+fib[-2])
    return fib[n]

def rowFib(budget,betSize,minbet,fibTries):
    numbers = []
    budgetPreSpin = budget
    randomNumber = spin()
    numbers.append(randomNumber)
    budget += (is1stRow(randomNumber) * minbet * betSize * fibonacci(fibTries))
    if budgetPreSpin <= budget:
        lastIsWin = True 
        fibTries = 0
    else:
        lastIsWin= False
        fibTries+=1
    return numbers,budget,lastIsWin,fibTries

def brFib(numberToAnalyze,budget,betSize,minbet,fibTries):
    numbers = []
    if isRed(numberToAnalyze) > 0:
        budgetPreSpin = budget
        randomNumber = spin()
        numbers.append(randomNumber)
        budget += (isBlack(randomNumber) * minbet * betSize * (fibonacci(fibTries)+1))
        if budgetPreSpin <= budget:
            lastIsWin = True 
            fibTries = 0
        else:
            fibTries+=1
            lastIsWin = False
    else:
        budgetPreSpin = budget
        randomNumber = spin()
        numbers.append(randomNumber)
        budget += (isRed(randomNumber) * minbet * betSize * (fibonacci(fibTries)+1))
        if budgetPreSpin <= budget:
            lastIsWin = True 
            fibTries = 0
        else:
            fibTries+=1
            lastIsWin= False
    return numbers,budget,lastIsWin,fibTries    
    
