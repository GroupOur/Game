from valizzka_helperFunctions import *


def Game():
<<<<<<< HEAD:valizzka_Game.py
=======
    """
    User interface to play the game
    Prints everything on console
    """
>>>>>>> master:valizzka_Game.py
    fairyTale()
    difficulty = setDifficulty()
    numbers = genNumbers(difficulty)
    # change easy to different
    tasks = {"ulam": (isUlam, "число Улама"), "lucky": (
<<<<<<< HEAD:valizzka_Game.py
        None, "вдале число"), "prime": (isPrime, "просте чило")}
=======
        None, "вдале число"), "prime": (None, "просте чило")}
>>>>>>> master:valizzka_Game.py
    counter, end, total, goal = 1, 15, 0, 10
    while counter < end + 1 and total < goal:
        current_task = genTask()
        reward = playLevel(counter, tasks[current_task], numbers, difficulty)
        total += reward
        print("\nЦя битва принесла вам профіт у", reward,
              'балів. Ваша загальна кількість балів становить', total, end="\n\n\n")
        counter += 1
    if counter == end+1:
        print("Ви не впоралися із заданням: Землю захоплено")
    elif goal == total:
        print("Ви впоралися із заданням: Землю врятовано!")


if __name__ == "__main__":
    Game()
