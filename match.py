import baseGame as bg

class Match:
    endScore = 0
    averageScore = 0
    endI = 0
    def __init__(self, budget, tries,minbet,stop):
      self.budget = budget
      self.tries = tries
      self.minbet = minbet
      self.stop = stop
    def sexMasLin(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        masTries = 0
        while (self.tries >= i) and (self.budget > (self.minbet*5 * pow(2,masTries))):
            if lastIsWin:
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is1stSex(randomNumber) * self.minbet)
                self.budget += (bg.is2ndSex(randomNumber) * self.minbet)
                self.budget += (bg.is3rdSex(randomNumber) * self.minbet)
                self.budget += (bg.is4thSex(randomNumber) * self.minbet)
                self.budget += (bg.is5thSex(randomNumber) * self.minbet)
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget else False
            else:
                numberToAnalyze = bg.numberToAnalyze(lastNumbers)
                n,b,l,m = bg.masanielloLin(numberToAnalyze,self.budget,5,self.minbet,masTries)
                self.budget = b
                lastNumbers += n
                lastIsWin = l
                masTries = m    
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def MDPMasLin(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        masTries = 0
        while (self.tries >= i) and (self.budget > (self.minbet*5 * pow(2,masTries))):
            if lastIsWin:
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is1to18(randomNumber) * self.minbet)
                self.budget += (bg.is1stCol(randomNumber) * self.minbet)
                self.budget += (bg.is2ndCol(randomNumber) * self.minbet)
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget+2 else False
            else:
                numberToAnalyze = bg.numberToAnalyze(lastNumbers)
                n,b,l,m = bg.masanielloLin(numberToAnalyze,self.budget,5,self.minbet,masTries)
                self.budget = b
                lastNumbers += n
                lastIsWin = l
                masTries = m
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def sexMasStop(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        masTries = 0
        while (self.tries >= i) and (self.budget > (self.minbet*5 * pow(2,masTries))):
            if lastIsWin:
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is1stSex(randomNumber) * self.minbet)
                self.budget += (bg.is2ndSex(randomNumber) * self.minbet)
                self.budget += (bg.is3rdSex(randomNumber) * self.minbet)
                self.budget += (bg.is4thSex(randomNumber) * self.minbet)
                self.budget += (bg.is5thSex(randomNumber) * self.minbet)
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget else False
            else:
                if masTries == self.stop:
                    masTries = 0
                    lastIsWin = True
                else:
                    numberToAnalyze = bg.numberToAnalyze(lastNumbers)
                    n,b,l,m = bg.masanielloLin(numberToAnalyze,self.budget,5,self.minbet,masTries)
                    self.budget = b
                    lastNumbers += n
                    lastIsWin = l
                    masTries = m
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def MDPMasLinStop(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        masTries = 0
        while (self.tries >= i) and (self.budget > (self.minbet*5 * pow(2,masTries))):
            if lastIsWin:
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is1to18(randomNumber) * self.minbet)
                self.budget += (bg.is1stCol(randomNumber) * self.minbet)
                self.budget += (bg.is2ndCol(randomNumber) * self.minbet)
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget+2 else False
            else:
                if masTries == self.stop:
                    masTries = 0
                    lastIsWin = True
                else:
                    numberToAnalyze = bg.numberToAnalyze(lastNumbers)
                    n,b,l,m = bg.masanielloLin(numberToAnalyze,self.budget,5,self.minbet,masTries)
                    self.budget = b
                    lastNumbers += n
                    lastIsWin = l
                    masTries = m
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def lovel91Mas(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        masTries = 0
        numlist = [25,26,27,28,29,30,31,32,33,34]
        while (self.tries >= i) and (self.budget > (self.minbet * 3 * pow(2,masTries))):
            if lastIsWin:
                # x sulle prime due righe e 0,1x su 10 numeri nella terza riga 
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is1stRow(randomNumber) * self.minbet)
                self.budget += (bg.is2ndRow(randomNumber) * self.minbet)
                self.budget += (bg.isInNumbers(randomNumber,numlist) * (self.minbet/len(numlist)))
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget else False
            else:
                numberToAnalyze = bg.numberToAnalyze(lastNumbers)
                n,b,l,m = bg.masanielloLin(numberToAnalyze,self.budget,3,self.minbet,masTries)
                self.budget = b
                lastNumbers += n
                lastIsWin = l
                masTries = m
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def lovel91Stop(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        masTries = 0
        numlist = [25,26,27,28,29,30,31,32,33,34]
        while (self.tries >= i) and (self.budget > (self.minbet * 3 * pow(2,masTries))):
            if lastIsWin:
                # x sulle prime due righe e 0,1x su 10 numeri nella terza riga 
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is1stRow(randomNumber) * self.minbet)
                self.budget += (bg.is2ndRow(randomNumber) * self.minbet)
                self.budget += (bg.isInNumbers(randomNumber,numlist) * (self.minbet/len(numlist)))
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget else False
            else:
                if masTries == self.stop:
                    masTries = 0
                    lastIsWin = True
                else:
                    numberToAnalyze = bg.numberToAnalyze(lastNumbers)
                    n,b,l,m = bg.masanielloLin(numberToAnalyze,self.budget,3,self.minbet,masTries)
                    self.budget = b
                    lastNumbers += n
                    lastIsWin = l
                    masTries = m
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def lovel91(self):
        i = 0
        lastNumbers = []
        numlist = [25,26,27,28,29,30,31,32,33,34]
        while (self.tries >= i) and (self.budget > (self.minbet * 3 )):
                # x sulle prime due righe e 0,1x su 10 numeri nella terza riga 
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is1stRow(randomNumber) * self.minbet)
                self.budget += (bg.is2ndRow(randomNumber) * self.minbet)
                self.budget += (bg.isInNumbers(randomNumber,numlist) * (self.minbet/len(numlist)))
                i+=1
                self.averageScore += self.budget
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def finalinoMas(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        masTries = 0
        while (self.tries >= i) and (self.budget > (self.minbet * 5 * pow(2,masTries))):
            if lastIsWin:
                # 3x sulla 2 colonna e 2x sulla terza riga
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is2ndCol(randomNumber) * self.minbet * 3)
                self.budget += (bg.is3rdRow(randomNumber) * self.minbet * 2)
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget else False
            else:
                numberToAnalyze = bg.numberToAnalyze(lastNumbers)    
                n,b,l,m = bg.masanielloLin(numberToAnalyze,self.budget,5,self.minbet,masTries)
                self.budget = b
                lastNumbers += n
                lastIsWin = l
                masTries = m
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def finalinoFib(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        fibTries = 0
        while (self.tries >= i) and (self.budget > (self.minbet * 5 * bg.fibonacci(fibTries))):
            if lastIsWin:
                # 3x sulla 2 colonna e 2x sulla terza riga
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is2ndCol(randomNumber) * self.minbet * 3)
                self.budget += (bg.is3rdRow(randomNumber) * self.minbet * 2)
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget else False
            else:
                n,b,l,f = bg.rowFib(self.budget,5,self.minbet,fibTries)
                self.budget = b
                lastNumbers += n
                lastIsWin = l
                fibTries = f
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
    def finalinoFibBR(self):
        i = 0
        lastIsWin = True
        lastNumbers = []
        fibTries = 0
        while (self.tries >= i) and (self.budget > (self.minbet * 5 * (bg.fibonacci(fibTries)+1))):
            if lastIsWin:
                # 3x sulla 2 colonna e 2x sulla terza riga
                budgetPreSpin = self.budget
                randomNumber = bg.spin()
                lastNumbers.append(randomNumber)
                self.budget += (bg.is2ndCol(randomNumber) * self.minbet * 3)
                self.budget += (bg.is3rdRow(randomNumber) * self.minbet * 2)
                i+=1
                self.averageScore += self.budget
                lastIsWin = True if budgetPreSpin <= self.budget else False
            else:
                numberToAnalyze = bg.numberToAnalyze(lastNumbers)
                n,b,l,f = bg.brFib(numberToAnalyze,self.budget,5,self.minbet,fibTries)
                self.budget = b
                lastNumbers += n
                lastIsWin = l
                fibTries = f
        self.endScore = self.budget
        self.averageScore = self.averageScore / i
        self.endI = i
        return(round(self.endScore),round(self.averageScore),self.endI)
