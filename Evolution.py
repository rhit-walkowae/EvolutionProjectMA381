import random


def findFitnessScore(genomeList:list):
    total = 0
    for n in genomeList:
        total+=n

    return total

class individual:
    def __init__(self,g_arr:list) -> None:
        self.genome = g_arr
        self.fitnessScore = findFitnessScore(g_arr) 



def generateFirstPopulation(popSize:int,genomeSize:int):

    individualList = []
    for x in range(popSize):
        num_zeros = random.randint(0,genomeSize)
        num_ones = genomeSize - num_zeros

        listORandomBinary = [0]*num_zeros + [1]*num_ones
        random.shuffle(listORandomBinary)

        individualList.append(individual(listORandomBinary))

    return individualList


def evaluate(popList:list[individual]):
    popList.sort(key= lambda x: x.fitnessScore, reverse=True)
    
#roulette Wheel Selection
def selection(selectionPressure:int,popList:list[individual]):
    
    pass


def main():
   gen_zero = generateFirstPopulation(10,10)
   evaluate(gen_zero)
   for i in range(len(gen_zero)):
        print(gen_zero[i].fitnessScore)


main()