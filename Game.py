from helperFunctions import *


def Game():
    fairyTail()
    difficulty = setDifficulty()
    numbers = genNumbers(difficulty)
    tasks = {"ulam": isUlam}
