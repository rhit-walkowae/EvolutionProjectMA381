from Evolution import*
import csv
import matplotlib.pyplot as plt


#from Evolution
population = generateFirstPopulation(10,10)
p = population
fields =["Average","Best"]
rows = []
for x in range(50):
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

    plt.plot(generations,best, Label = "BEST")
    plt.plot(generations,avg,Label = "AVERAGE")

    plt.legend()
    plt.xlabel('Generations')
    plt.ylabel('Fitness')

    plt.savefig("plot.png")
    plt.show()