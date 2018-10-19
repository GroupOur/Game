<<<<<<< HEAD:valizzka_helperFunctions.py
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


def isPrime(number):
    """ (int) -> bool

    Precondition: given number must be between 0 and 100

    This funcion returns true if a number less than 100 is prime and false otherwise.

    >>> isPrime(2)
    True
    >>> isPrime(5)
    True
    >>> isPrime(40)
    False
    """
    prime = [2]
    for iterator in range(2, 100):
        if pow(2, iterator, iterator) == 2:
            prime.append(iterator)      
    return number in prime    


def fairyTale():
    print("In the kingdom of Logos you are the last Mathemagician - the keeper of forgotten knowledge. Everyone has given up on theoretical mathematics in favour of computer science, big data and quantum physics. Prove that your field of study is no less competent by correctly matching the numbers with their respectable set as fast as possible. You will have to deal with prime, lucky and Ulam numbers. In order to win you will have to earn 10 points in 15 turns or less. You recieve one point if your answer is correct and lose two if it is incorrect. Good luck, you'll need it!", end="\n\n\n")


def setDifficulty():
    """
    Some kind of user interface
    returns amount of numbers to be guessed
    """
    print("Choose the difficulty level")
    print("< 0-easy 1-normal 2-hard >")
    difficulty = input("Print here: ")
    if difficulty == "0" or difficulty == "easy":
        return 25
    elif difficulty == "1" or difficulty == "normal":
        return 50
    elif difficulty == "2" or difficulty == "hard":
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
=======
def isUlam(number):
    """
    (0<int<=100) ---> bool
    Checks if the number is ulam number. Returns True if so, False if else.
    >>> isUlam(5)
    False
    >>> isUlam(2)
    True
    >>> isUlam(1)
    True
    >>> isUlam(49)
    False
    """
    if number < 3:
        return True
    ulams = [1, 2]
    last_elemIndex = len(ulams)-1
    while ulams[last_elemIndex] < number:
        try_ulams = []
        for i in range(last_elemIndex):
            for j in range(i+1, last_elemIndex+1):
                try_number = ulams[i]+ulams[j]
                if try_number not in ulams:
                    try_ulams.append(try_number)
        bestElem = min(try_ulams)
        while try_ulams.count(bestElem) != 1:
            for i in range(try_ulams.count(bestElem)):
                try_ulams.remove(bestElem)
            bestElem = min(try_ulams)
        ulams.append(bestElem)
        last_elemIndex += 1
    if ulams[last_elemIndex] == number:
        return True
    return False

def isPrime(number):
    """ (int) -> bool
     Precondition: given number must be between 0 and 100
     This funcion returns true if a number less than 100 is prime and false otherwise.
     >>> isPrime(2)
    True
    >>> isPrime(5)
    True
    >>> isPrime(40)
    False
    """
    prime = [2]
    for iterator in range(2, 100):
        if pow(2, iterator, iterator) == 2:
            prime.append(iterator)      
    return number in prime    

def fairyTale():
    print("Нашу землю ось-ось захоплять інопланетяни! Їхні технології кращі за наші,проте вони не знають ні чисел Улама, ні простих чисел, ні вдалих! Ваше завдання - захистити людство шляхом класифікації даних вам чисел за цими ознаками. Ви виграєте, якщо за 15 або і менше ходів наберете 10 балів. За кожну правильну відповідь вам нараховується один бал, за кожну неправильну знімається два бали Хай щастить!", end="\n\n\n")


def setDifficulty():
    """
    (nothing)-->int
    User interface to pick up difficulty
    Returns amount of numbers to be guessed
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
    """
    (int,list,list,int)--->int
    User interface to choose answer
    Returns the ammount of points you earned based on difficulty level, current task, 
    current points, current list of numbers, user`s answer.
    """
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
    """
    (list,int,int)--->modifies input list
    Removes given number from the given list and 
    randomly picks up a new different from others
    number and adds it to the list
    """
    import random
    list_numbers.remove(number)
    new_number = random.randrange(1, difficulty+1)
    while new_number in list_numbers:
        new_number = random.randrange(1, difficulty+1)
    list_numbers.append(new_number)


def genTask():
    """
    (nothing)-->str
    Returns randomly chosen task
    """
    import random
    return random.choice(["ulam", "lucky", "prime"])


def genNumbers(difficulty):
    """
    (int)--->list
    Given difficulty (range to pick up numbers from) returns randomly chosen list of
     15 different numbers
    """
    import random
    numbers = []
    number = 0
    for i in range(15):
        number = random.randrange(1, difficulty+1)
        while number in numbers:
            number = random.randrange(1, difficulty+1)
        numbers.append(number)
    return numbers
>>>>>>> master:valizzka_helperFunctions.py
