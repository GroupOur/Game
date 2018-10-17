from helperFunctions import *


def Game():
    fairyTail()
    difficulty = setDifficulty()
    numbers = genNumbers(difficulty)
    # change easy to different
    tasks = {"ulam": isUlam, "lucky": None, "easy": None}
    counter, end, total, goal = 0, 15, 0, 10
    while counter < end +1 and total<goal
