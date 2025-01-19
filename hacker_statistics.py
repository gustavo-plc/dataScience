import random

import numpy as np

#manually setting the seed:

np.random.seed(123)

n = np.random.rand()  #pseudo-random numbers - PC chooses the seed
print(n)

# SIMULATING A DICE

dice = np.random.randint(1,7)
print(dice)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step -= 1
elif dice in {3, 4, 5} :
    step += 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

# RANDOM STEPS SIMULATING A FLIPPING A COIN 10 TIMES

#defining a list to store the results
outcomes = list()

for x in range (10):
    #in each iteration, the coin variable will be
    #updated

    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')

print(outcomes)
print()

# A RANDOM WALK EXAMPLE IN THIS HEADS ANS TAILS EXAMPLE

tails = [0] #at the start I've not thrown any coins yet

for x in range(10):
    coin = np.random.randint(0, 2) #a coin is flipped and the result is stored (0 or 1)
    tails.append(tails[x] + coin) #the result is appended to the list tails updating its last result

print(tails)
print()
# THE EXAMPLES ABOVE SHOWED HOW TO
# TRANSFORM A BUNCH OF STEPS INTO A RANDOM WALK


#another example

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)