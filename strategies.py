from match import Match
import matplotlib.pyplot as plt
import statistics
import time

names = {
"sexMasLin" : "Sextain method with R/B Masaniello",
"sexMasStop" : "Sextain method with R/B Masaniello with stop",
"lovel91Mas" : "Lovel91 method with R/B Masaniello",
"lovel91Stop" : "Lovel91 method with R/B Masaniello with Stop",
"lovel91" : "Lovel91 method with no Masaniello",
"MDPMasLin" : "MDP method with R/B Masaniello",
"MDPMasLinStop" : "MDP method with R/B Masaniello with Stop",
"finalinoMas" : "Finalino method with R/B Masaniello",
"finalinoFib" : "Finalino method with Fibonacci Sextain",
"finalinoFibBR" : "Finalino method with Fibonacci R/B"
}

class Strategy:
    matches = []
    results = []

    #To return
    bestScore = 0
    worstScore = 0
    averageEndScore = 0
    standardDeviation = 0
    unpredictability = 0    
    
    def __init__(self, code, budget, tries,minbet,matchesNumber,stop):
      self.code = code
      self.name = names[self.code]
      self.budget = budget
      self.tries = tries
      self.minbet = minbet
      self.matchesNumber = matchesNumber
      self.stop = stop

    def start(self):
        for _ in range (0,self.matchesNumber):
            self.matches.append(
                Match(
                    self.budget,
                    self.tries,
                    self.minbet,
                    self.stop)
                    )
        for match in self.matches:
            self.results.append(getattr(match,self.code)())
            
        
    def calc(self):
        self.bestScore = max(self.results,key=lambda x:x[0])[0]
        self.worstScore = min(self.results,key=lambda x:x[0])[0]
        self.averageEndScore = sum(x for x,_,_ in self.results)/len(self.results)
        self.standardDeviation = statistics.stdev([x for x,_,_ in self.results])
        self.unpredictability = (statistics.stdev([y for _,y,_ in self.results]))/self.budget


    def plot(self):
        x = []
        y = []

        x = range(0,len(self.results))
        y = ([f for f,_,_ in self.results])
        plt.figure(figsize=(18,8))
        plt.plot(x,y)
        plt.plot([0, len(self.matches)], [self.averageEndScore, self.averageEndScore], 'k-', lw=2)
        plt.plot([0, len(self.matches)], [self.budget, self.budget], 'r-', lw=2)
        plt.title(f"{self.name} - Average budget: {self.averageEndScore} - Max: {self.bestScore} - Min: {self.worstScore}")
        plt.ylabel(f"Earning matches: {sum(map(lambda m : m>self.budget, y))}({sum(map(lambda m : m>self.budget, y))*100/len(y)}%) - Starting budget: {self.budget} - Spins: {self.tries} - Min. Bet: {self.minbet} ")
        plt.xlabel(f"Standard Deviation: {self.standardDeviation} - Unpredictability coef.: {self.unpredictability}")
        plt.savefig(f"graphs/{self.code}_{int(time.time())}.png")