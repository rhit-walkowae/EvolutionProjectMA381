from Evolution import*
import csv
import matplotlib.pyplot as plt


#from Evolution
popS = int(input('Enter number of population members: '))
genomeS = int(input('Enter number of genomes(even only): '))
genS = int(input('Enter number of generations to graph: '))

population = generateFirstPopulation(popS,genomeS)
p = population
fields =["Average","Best"]
rows = []
for x in range(genS):
    results = simulateGeneration(p)
    p = results.get("NextGen")
    a = results.get("Average")
    b = results.get("Best")
    rows.append([a,b])

with open("data.csv",'w',newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerow(rows)

    generations = []
    best = []
    avg = []
    n = 0
    for r in rows:
        n+=1
        generations.append(n)
        best.append(r[1])
        avg.append(r[0])

    plt.plot(generations,best, label = "BEST")
    plt.plot(generations,avg,label = "AVERAGE")

    plt.legend()
    plt.xlabel('Generations')
    plt.ylabel('Fitness')

    plt.savefig("plot.png")
    plt.show()