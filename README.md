# EvolutionProjectMA381
This is my submission for Rose-Hulman's MA381 project.
The project I chose was Evolution. For this model I will simulate a simple species evolving over generations. The details are as follows:

* Each organisms is represented by object that stores that individual organisms genome and the fitness of that genome

* The genome is a list of 1's and 0's the fitness score it the sum of all the ones so for a **n** length genome the max fitness is **n**
* This uses the individual's fitness score ( **f** ) and the sum of all fitness scores ( **SUM( f<sub>i</sub> )** ) to give each individual a probability of being selected **p(f) = f / SUM( f<sub>i</sub> )**. Half of the generation is killed with higher fitness scores being more probable to survive.
* This model uses a Diploid Reproductive mechanisms for generating offspring by crossing over genes from the surviving individuals after selection. 
* Offspring have a chance to be slightly mutated every generation, however a offspring will have deleterious mutations meaning on average the offspring will less fit on average. 

To better illustrate this imagine the example of 4 individuals with the following genomes of length 5:
 1. [1,0,0,0,1]
 2. [1,1,1,1,0]
 3. [0,1,0,0,0]
 4. [1,1,0,0,0]

 The following fitness would be:
 1. 2
 2. 4
 3. 1
 4. 2

The sum of all these is 9. This means the following probabilities for each to survive long enough and make offspring is:
1. 2/9
2. 4/9
3. 1/9
4. 2/9

When Selection is ran the individual **4** and **2** are selected to survive. And the cross their Genomes when having kids 4 gives their two offspring their first 3 genes and 2 gives 4's offspring their last 2 genes. 2 gives their offspring their first 3 genes and 4 gives 2's two offspring their last 2 genes. so we end up with

1. Child of 4: [**1,1,0**,1,0]
2. Child of 4: [**1,1,0**,1,0]
3. Child of 2: [**1,1,1**,0,0]
4. Child of 2: [**1,1,1**,0,0]