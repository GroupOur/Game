lst_prime = []
lst_not_prime = []
lst_ulam = []
lst_not_ulam = []
lst_lucky = []
lst_not_lucky = []


def Ulam(lst_ulam=[], lst_not_ulam=[], number=100):
    """
    (list,list,int)--->nothing
    Default values : [],[],100
    For numbers in range from 1 to 100 modifies input lists:
    one list for ulam numbers, another for not ulam numbers
    """
    if number < 1:
        lst_ulam, lst_not_ulam = [], []
    elif number == 2:
        lst_ulam, lst_not_ulam = [2], []
    elif number == 2:
        lst_ulam, lst_not_ulam = [2, 3], []
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
        if bestElem not in lst_ulam:
            lst_ulam.append(bestElem)
        last_elemIndex += 1
    for elem in range(1, number+1):
        if elem not in ulams:
            lst_not_ulam.append(elem)


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
    global lst_ulam
    return number in lst_ulam


def Prime(lst_prime, lst_not_prime):
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
    lst_prime.append(2)
    lst_not_prime.append(1)
    for iterator in range(2, 100):
        if pow(2, iterator, iterator) == 2:
            lst_prime.append(iterator)
        else:
            lst_not_prime.append(iterator)


def isPrime(num):
    global lst_prime
    return num in lst_prime


def Lucky(lst_lucky, lst_not_lucky):
    lst = [i for i in range(101)]
    x = 2
    lst[0] = -1
    while(x < len(lst)):
        for i in range(x, len(lst), x):
            lst[i] = False
        j = 1
        while (j < len(lst)):
            if lst[j] == False:
                lst_not_lucky.append(lst[j])
                lst.remove(lst[j])
            j += 1
        print(x)
        print(lst)
        x = lst[x]

    for i in lst:
        lst_lucky.append(i)


def isLucky(num):
    global lst_lucky
    return num in lst_lucky


Prime(lst_prime, lst_not_prime)
Lucky(lst_lucky, lst_not_lucky)
print(lst_prime)
print(lst_lucky)


def GenNumbers(lst):
    import random
    numbers = []
    for i in lst:
        numbers.append(i.num)
    number = random.randrange(1, 100)
    while number in numbers:
        number = random.randrange(1, 100)
    return number
