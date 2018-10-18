def isUlam(number):
    """
    (number) --> bool
    0 < number <= 100
    Checks if number is Ulam number
    >>> isUlam(5)
    False
    >>> isUlam(9)
    False
    >>> isUlam(72)
    True
    """
    ulams = (1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38,
             47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99)
    return number in ulams


def fairyTail():
    print("Нашу землю ось-ось захоплять інопланетяни! Їхні технології кращі за наші,проте вони не знають ні чисел Улама, ні простих чисел, ні вдалих! Ваше завдання - захистити людство шляхом класифікації даних вам чисел за цими ознаками. Ви виграєте, якщо за 15 або і менше ходів наберете 10 балів. За кожну правильну відповідь вам нараховується один бал, за кожну неправильну знімається два бали Хай щастить!", end="\n\n\n")


def setDifficulty():
    """
    Some kind of user interface
    returns amount of numbers to be guessed
    """
    print("Виберіть рівень розвитку інопланетних загарбників")
    print("< 0-легко 1-нормально 2-важко >")
    difficulty = input("Print here: ")
    if difficulty == "0" or difficulty == "легко":
        return 25
    elif difficulty == "1" or difficulty == "нормально":
        return 50
    elif difficulty == "2" or difficulty == "важко":
        return 100
    else:
        return setDifficulty()


def playLevel(counter, task, list_numbers, difficulty):
    print("\n\nБитва №", counter, end="\n\n")
    print(*list_numbers, end="\n\n")
    user_number = 0
    try:
        while user_number not in list_numbers:
            user_number = input("Із вище наведених чисел виберіть " +
                                task[1] + ". Якщо такого числа нема натисніть \"Enter\". --> ")
            user_number = int(user_number)
        updateNumbers(list_numbers, user_number, difficulty)
    except:
        if user_number == "":
            for elem in list_numbers:
                if task[0](elem):
                    return -2
            return 1
    else:
        if task[0] == None:
            return 2
        if task[0](user_number):
            return 1
        else:
            return -2


def updateNumbers(list_numbers, number, difficulty):
    import random
    list_numbers.remove(number)
    new_number = random.randrange(1, difficulty+1)
    while new_number in list_numbers:
        new_number = random.randrange(1, difficulty+1)
    list_numbers.append(new_number)


def genTask():
    import random
    return random.choice(["ulam", "lucky", "easy"])


def genNumbers(difficulty):
    import random
    numbers = []
    number = 0
    for i in range(15):
        number = random.randrange(1, difficulty+1)
        while number in numbers:
            number = random.randrange(1, difficulty+1)
        numbers.append(number)
    return numbers
