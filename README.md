# AI-Sudoku-Solver

----------------------------------------------------------
-- This is the README File for my evolutionary algorithm--
----------------------------------------------------------

This algorithm uses evolutionary logic to create an algorithm to solve a number Sudoku puzzle.
This is done by filling in the puzzle with a random permutation of digits from 1 to 9 and then
analyzing these generated puzzles(population) with a fitness function, then sorting out the population
according ranked by best fitness.

---------------------------------------------------------------------------------------------------------
How to Run:

Open a command prompt and go to the current directory and type in "coursework.py" in the command line.

The program will run and display the board before it has been solved and after with the fitness and population
specified during each run.

**
To add a puzzle you must create a list of lists that represent the puzzles rows and then insert the fixed
values in their positions and fill the rest of the puzzle with zeros which represent the missing numbers.

Then add that puzzle to the evolve function to be run. 
**

### Solution Space 
The Solution Space is all possible combinations of Sudoku grids (partially solved and complete)

### Solution Representation
The Solution Representation is a Sudoku grid where each line contains the digits from 1-9 without repetition.

### Fitness Function 
To calculate the fitness of each Sudoku puzzle I wrote an algorithm to take each row, column and sub grid of each puzzle and check if the sum is equal to 45 which is the sum of a solved Sudoku puzzle row, column, and sub gird without any duplicates, if the sum is not equal to 45 then the fitness is increased by 1, else decreased by 1. And at the end the fitness is printed out as a percentage where the higher the percentage the better the fitness score.
1 + 2 + 3 … + 9 = 45

### Crossover Operator
The crossover operator used was a basic crossover where I took a random row from two parents in the population and stored the index of those rows, and then took the row and swapped them from parent 1 to parent 2 and vice versa and then returned one of the parents randomly.

### Mutation Operator
The mutation operator I used was a simple one where I take a random value from a row and swap it with a random integer between 1 and 9 repeatedly but avoiding the fixed numbers in the board, and I did that by storing the index of each non-fixed number and chose from there.

### Initialising the Population
I initialised the population by selecting the grid and finding all zero values which are the missing numbers and replaced them with any random number between 1 and 9 and I did that for the specified population number, so 10, 100, 1000, 10000.

### Selection and Replacement Methods
For Selection and Replacement, The entire population of grids is ranked by the fitness function. The grid with the highest fitness is selected and the one with the worst fitness is replaced by a new random grid.

### Termination Criterion
The Genetic Algorithm runs until a solution is found or the maximum number of generations is reached. Once terminated it will return the best fitness and the best puzzle representation and print them out to the screen.
