import random
import numpy as np


def findFitnessScore(genomeList:list):
    total = 0
    for n in genomeList:
        total+=n

    return total

class individual:
    def __init__(self,g_arr:list) -> None:
        self.genome = g_arr
        self.fitnessScore = findFitnessScore(g_arr) 



def generateFirstPopulation(popSize:int,genomeSize:int)->list[individual]:
    ''' takes the populations desired size and the desired sixe of each '''
    individualList = []
    for x in range(popSize):
        num_ones = random.randint(0,genomeSize- genomeSize/2) 
        num_zeros = genomeSize - num_ones

        listORandomBinary = [0]*num_zeros + [1]*num_ones
        random.shuffle(listORandomBinary)

        individualList.append(individual(listORandomBinary))

    return individualList


def evaluate(popList:list[individual]):
    popList.sort(key= lambda x: x.fitnessScore, reverse=True)
    
#roulette Wheel Selection
def selection(selectionPressure:int,popList:list[individual])->dict:
    halfSize = int(len(popList)/2)
    sum_fitness = 0
    Best = -1
    num_inds = 0
    for x in popList:
        num_inds +=1
        f = x.fitnessScore
        sum_fitness += f
        if(f > Best):
            Best = f
    w = []
    for i in popList:
        w.append(i.fitnessScore/sum_fitness)
    selectedList = np.random.choice(popList,halfSize,replace = False,p = w)
    d = {"survivors":selectedList,"Best":Best,"Average":sum_fitness/num_inds}
    return d

def crossoverOffspring(survivorList: list[individual]):
    offspring =[]
    size_genome = len(survivorList)
    halfLength = int(size_genome/2)
    for i in range(len(survivorList)):
        tempList = survivorList[i].genome[:halfLength]
        tempList2 = survivorList[i].genome[halfLength:]
        tempList += survivorList[i-1].genome[halfLength:]
        tempList2 += survivorList[i-1].genome[:halfLength]
        mutationIndex = random.randint(0,size_genome-1)
        if(tempList[mutationIndex] == 1):
            tempList[mutationIndex] == 0
        else:
            tempList[mutationIndex]== 1
        if(tempList2[mutationIndex] == 1):
            tempList[mutationIndex] == random.randint(0,1)
        offspring.append(individual(tempList))
        offspring.append(individual(tempList2))

        

    return offspring


   
def simulateGeneration(pList:list)->dict:
    '''This function takes a list of individuals and returns a dictionary with KEYS
    "NextGen" --> the crossover offspring of input generation
    "Average" --> the average fitness of the input generation
    "Best" --> the best fitness score within the input generation'''
    halfLen = int(len(pList)/2)
    selectionDict = selection(halfLen,pList)
    selectedList = selectionDict.get("survivors")
    Best = selectionDict.get("Best")
    Average = selectionDict.get("Average")
    nextGen = crossoverOffspring(selectedList)
    result = {"NextGen":nextGen,"Average":Average,"Best":Best}
    return result

