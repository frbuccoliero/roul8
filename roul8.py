import matplotlib.pyplot as plt
from match import Match
import strategies
from strategies import Strategy

print ("Welcome to my Roulette's strategy simulator")
print ("Credits: Francesco Buccoliero @frbuccoliero\n")

for strategy in strategies.names:
    print(f"{strategy} - {strategies.names[strategy]}")

code = None
while not code or not code in strategies.names.keys(): 
    code = input("Pick a strategy to test: ")

budget = int(input("Set a starting budget: "))
tries = int(input("Number of spins: "))
minbet = float(input("Minimum bet: "))
matchesNumber = int(input("Number of simulations: "))
stop = int(input("Max number of Masaniello spins: ")) if "Stop" in code else 0    

strategy = Strategy(code,budget,tries,minbet,matchesNumber,stop)
strategy.start()
strategy.calc()
strategy.plot()