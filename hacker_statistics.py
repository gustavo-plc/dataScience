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