import random

def diceroll():
    score = 0
    stop = False
    for i in range(3):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        if x == y:
            stop = True
        elif stop == True:
            score = 0
        else:
            score += x + y
    return score

print("Lucas score is ", diceroll())
print("And Samuels score is ", diceroll())