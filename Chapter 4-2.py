import random
numberOfSteaks = 0
numberOfFlips = 100
numberOfTests = 10000

def createFlipsList():
    flips = []
    for i in range(numberOfFlips):
        if random.randint(0, 1) == 0:
            flip = 'H'
        else:
            flip = 'T'
        flips.append(flip)
    return flips


print(createFlipsList())
