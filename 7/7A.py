import statistics
import math

def fuel(d):
    return math.floor(0.5+d*(d+1)/2)
def distance(x,g):
    return abs(x - g)




with open("7Ainput.txt") as file:
    positions = [int(x) for line in file for x in line.split(",")]

goal = math.floor(statistics.mean(positions))
print(goal)
print(sum(map(lambda x: fuel(distance(x, goal)), positions)))
print(positions[-1:])