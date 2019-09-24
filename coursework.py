#
# SUDOKU EVOLUTIONARY ALGORITHM  
#

from random import choice, random, randint
import copy

### EVOLUTIONARY ALGORITHM ###

def evolve(board, ind):
	for popsize in POPULATION_SIZE:
		print("Population size:  ", popsize)
		population = fill_pop(board, popsize) #initial population
		fitness_population = fitness_pop(population)
		best_FIT = []
		best_IND = []
		for _ in range(NUMBER_GENERATION):
			mating_pool = select_pop(population, fitness_population, popsize)
			offspring_population = crossover_pop(mating_pool, popsize)
			population = mutate_pop(ind, offspring_population) #enhanced population (crossover and mutation)
			fitness_population = fitness_pop(population)
			best_ind, best_fit = best_pop(population, fitness_population) #getting the best fitness and puzzle
			best_IND.append(best_ind)
			best_FIT.append((int(best_fit)))
			if best_fit == 100:
				break
		best_IND = sorted(best_IND, key=lambda ind_fit: ind_fit[1])
		best_FIT = sorted(best_FIT, key=int,reverse=True)
		print("fit:%3d %%" % (100 - best_FIT[0]))
	print("\n")
	
		
### POPULATION-LEVEL OPERATORS ###

def fill_pop(board, pop):
	"""The argument pop is the population number"""
	return [fill(board) for _ in range(pop)]

def fitness_pop(population):
	return [fitness_function(ind) for ind in population]

def crossover_pop(population, pop):
    return [ crossover(choice(population), choice(population)) for _ in range(pop) ]
	
def mutate_pop(ind, population):
    return [ mutate(ind, individual) for individual in population ]
	
def select_pop(population, fitness_population, pop):
    sorted_population = sorted(zip(population, fitness_population), key = lambda ind_fit: ind_fit[1])
    return [ individual for individual, fitness in sorted_population[:int(pop * TRUNCATION_RATE)] ]
	
def best_pop(population, fitness_population):
    return sorted(zip(population, fitness_population), key = lambda ind_fit: ind_fit[1])[0]

### INDIVIDUAL-LEVEL OPERATORS: REPRESENTATION & PROBLEM SPECIFIC ###

def fitness_function(board): 
	""" This function is used to calculate the fitness of the puzzle by checking if the sum of each row, column or subgird is equal to 45"""
	count = 0
	for x in range(0,N):
		if sum(board[x]) != 45:
			count += 1
		else:
			count -=1
	
	for y in range(0,N):
		if sum([row[y] for row in board]) != 45:
			count += 1
		else:
			count -=1			
	for i in range(0, 7, 3):
		for j in range(0, 7, 3):
			if sum(check_subgrid(board, i, j)) != 45:
				count += 1
			else:
				count -=1	

	return (count/27*100)

def fill(board):
	""" This function is used to fill a partial puzzle with random values """
	temp = copy.deepcopy(board)
	for x in range(0,N):
		for y in range(0, N):
			if temp[x][y] == 0:
				temp[x][y] = choice(numbers)
	return temp

def crossover(individual1, individual2):
	indv_copy1 = copy.deepcopy(individual1)
	indv_copy2 = copy.deepcopy(individual2)
	temp1 = []
	ind1 = 0
	leng = len(indv_copy1)
	leng2 = len(indv_copy2)
	temp2 = []
	ind2 = 0
	temp1 = indv_copy1[randint(0,leng-1)]
	ind1 = indv_copy1.index(temp1)
	temp2 = indv_copy2[randint(0,leng2-1)]
	ind2 = indv_copy2.index(temp2)
	indv_copy1[ind1] = temp2
	indv_copy2[ind2] = temp1
	choices = (indv_copy1, indv_copy2)
	return choice(choices)
	
def mutate(ind, individual):
	""" This function is to mutate an individual value that is not fixed by getting the index of all non-fixed values which is the argument ind"""
	res = []
	for ch in individual:
		if random() < MUTATION_RATE:
			num = choice(ind)
			if num != 0:
				ch[num] = randint(1,9)
			res.append(ch)
		else:
			ch
			res.append(ch)
	return res
		
### ### ###

def printBoard(board):
	""" This function is used to print out the sudoku board in a presentable manner """
	print("*********************")
	for x in range(0, 9):
		if x == 3 or x == 6:
			print("*********************")
		for y in range(0, 9):
			if y == 3 or y == 6:
				print("|", end=" ")
			print(board[x][y], end=" ")
		print()
	print("*********************")

### The Three Sudoku Puzzles ###

board1 = [[4,0,0,1,0,2,6,3,0],
		  [5,0,0,6,4,3,8,0,0],
		  [7,6,0,5,0,8,4,1,2],
		  [6,0,0,0,0,9,3,4,8],
		  [2,4,0,8,3,0,9,5,0],
		  [8,0,9,4,1,5,0,7,0],
		  [0,7,2,0,0,4,0,6,0],
		  [0,5,4,2,0,0,0,8,9],
		  [0,8,6,3,0,7,1,2,4]]

board2 = [[6,0,0,7,0,0,0,0,1],
          [7,0,0,0,0,9,2,0,0],
          [0,2,9,6,0,0,0,0,0],
          [0,5,7,0,3,6,1,0,4],
          [2,0,3,0,7,1,0,5,8],
          [1,8,0,2,9,0,0,6,3],
          [0,0,0,0,0,2,5,0,9],
          [4,9,6,3,0,0,8,0,0],
          [0,0,2,9,8,0,6,0,7]]

board3 = [[4,0,0,0,6,0,0,0,1],
		  [9,0,0,0,0,3,0,5,0],
		  [0,1,0,7,0,0,0,3,9],
		  [8,0,6,0,0,0,0,0,0],
		  [0,0,4,5,9,1,0,0,0],
		  [0,0,0,3,0,6,0,0,0],
		  [0,0,0,0,7,2,0,0,4],
		  [2,5,1,6,0,0,9,0,0],
		  [0,0,0,8,5,9,2,0,0]]

N=9
numbers = list(range(1,10))

### PARAMERS VALUES ###

POPULATION_SIZE = [10,100,1000,10000]
TRUNCATION_RATE = 0.5
MUTATION_RATE = 1/N
NUMBER_GENERATION = 100

ind1 = [] #index of all the non-fixed numbers in board1
for x in range(0,N):
	for y in range(0, N):
		if board1[x][y] == 0:
			ind1.append(board1[x].index(board1[x][y],y))
			ind1.append(0)
			
ind2 = [] #index of all the non-fixed numbers in board2
for x in range(0,N):
	for y in range(0, N):
		if board2[x][y] == 0:
			ind2.append(board2[x].index(board2[x][y],y))
			ind2.append(0)
			
ind3 = [] #index of all the non-fixed numbers in board3
for x in range(0,N):
	for y in range(0, N):
		if board3[x][y] == 0:
			ind3.append(board3[x].index(board3[x][y],y))
			ind3.append(0)
		
def check_subgrid(board, row, column):
	""" This function gets one subgrid of a board for a row and column """
	nineGrouping = []
	for i in range(row, row + 3):
		for j in range(column, column + 3):
			nineGrouping.append(board[i][j])
	return nineGrouping

### EVOLVE ###


for i in range(1,6):
	print("Run Number:  ", i)
	print("\n")
	print("BOARD 1:")
	evolve(board1, ind1)
	print("BOARD 2:")
	evolve(board2, ind2)
	print("BOARD 3:")
	evolve(board3, ind3)