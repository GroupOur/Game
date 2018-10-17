from helperFunctions import *


def Game():
    fairyTail()
    difficulty = setDifficulty()
    numbers = genNumbers(difficulty)
    # change easy to different
    tasks = {"ulam": (isUlam, "число Улама"), "lucky": (
        None, "вдале число"), "easy": (None, "просте чило")}
    counter, end, total, goal = 1, 15, 0, 10
    while counter < end + 1 and total < goal:
        current_task = genTask()
        reward = playLevel(counter, task[current_task], numbers, difficulty)
        total += reward
        print("\nЦя битва принесла вам профіт у", reward,
              'балів. Ваша загальна кількість балів становить', total, end="\n\n\n")
