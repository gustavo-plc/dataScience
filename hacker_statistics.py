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
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
print()

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
#
# TRANSFORMING THE PROBLEM INTO A DISTRIBUTION OF FINAL STEPS
# TO ANSWER THE MAIN QUESTION: WHAT IS THE CHANCE I'LL REACH
# 60 STEPS HIGH?
#
# THE WAY TO ANSWER THIS QUESTION IS TO TRANSFORM THE PROBLEM
# INTO A DISTRIBUTION OF STEPS

# this can be done because each random walk will end up in a different step,
# thus it can be treated as a distribution of final steps

#once we know the distribution, we can start calculating probability

final_tails = [] # will register the number of tails we end up with by flipping the coin
# 10x over and over again, lets do an example for 100 times.

# event: flipping a coin 10 times
# number of events: 10000

for x in range(10000): #for every event, the number of tails is reseted to zero. Because the event restarts
    tails = [0]
    for x in range(10): # loop that runs each of the 10 events
        coin = np.random.randint(0, 2) #flipping the coin
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, 10)
plt.show()

# EACH NUMBER IN THE FINAL_TAILS LIST IS THE NUMBER OF TIMES WE GOT TAILS IN A GAME OF 10 TOSSES
# THIS CAN BE TREATED AS A DISTRIBUTION THAT WE CAN VISUALIZE: IT CALLS FOR A HISTOGRAM!

# THE MORE WE INCREASE THE NUMBER OF EVENTS, THE MORE THE DISTRIBUTION CONVERGES TO A BELL-SHAPE


# Simulate multiple walks


# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :
    # Code from before
    random_walk = [0] #each simulation starts from the step 0
    for x in range(100) :
        step = random_walk[-1] #recovering the last step value
        dice = np.random.randint(1,7) #throwing the dice
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step) #adding the step result to the random_walk list
    # Append random_walk to all_walks
    all_walks.append(random_walk) # this line adds the entire random_walk list
    # to the all_walks list. This means that all_walks will contain each step of each walk


# Print all_walks
print(all_walks)

# VISUALIZING ALL WALKS: TRANSFORM TO AN NUMPY ARRAY

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()