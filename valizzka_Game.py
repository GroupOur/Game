from valizzka_helperFunctions import *


def Game():
    fairyTale()
    difficulty = setDifficulty()
    numbers = genNumbers(difficulty)
    # change easy to different
    tasks = {"ulam": (isUlam, "Ulam number"), "lucky": (
        None, "lucky number"), "prime": (isPrime, "prime number")}
    counter, end, total, goal = 1, 15, 0, 10
    while counter < end + 1 and total < goal:
        current_task = genTask()
        reward = playLevel(counter, tasks[current_task], numbers, difficulty)
        total += reward
        print("\nYou scored %i points" % reward,
              'Your total score is', total, end="\n\n\n")
        counter += 1
    if counter == end+1:
        print("You failed. From this day onwards, no one shall take you seriously")
    elif goal == total:
        print("You succeeded! Now that you have earned yourself a name, more and more people will be intimidated to learn about mathemagic!")


if __name__ == "__main__":
    Game()
