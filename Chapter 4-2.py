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


def testStreak(flips):
    headOrTail = flips[0]
    inARow = 0
    for i in range(1, numberOfFlips):
        if flips[i] == headOrTail:
            inARow += 1
            if inARow == 6:
                return True
        else:
            headOrTail = flips[i]
            inARow = 0
    return False


for i in range(numberOfTests):
    if testStreak(createFlipsList()) == True:
        numberOfSteaks += 1
print('La probabilité d\'avoir 6 tirages identiques de suite est de ' +
      str(numberOfSteaks*100/numberOfTests)+'%')
