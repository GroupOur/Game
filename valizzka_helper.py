lst_prime = []
lst_not_prime = []
lst_ulam = []
lst_not_ulam = []
lst_lucky = []
lst_not_lucky = []
MAX = 100


def Ulam(lst_ulam, lst_not_ulam, MAX):
    """
    (list,list,int)--->nothing
    For numbers in range from 1 to MAx modifies input lists:
    one list for ulam numbers, another for not ulam numbers
    """
    if MAX < 1:
        lst_ulam, lst_not_ulam = [], []
    elif MAX == 2:
        lst_ulam, lst_not_ulam = [2], []
    elif MAX == 2:
        lst_ulam, lst_not_ulam = [2, 3], []
    ulams = [1, 2]
    last_elemIndex = len(ulams)-1
    while ulams[last_elemIndex] < MAX:
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
    for elem in range(1, MAX + 1):
        if elem not in ulams:
            lst_not_ulam.append(elem)
        else:
            lst_ulam.append(elem)


def Prime(lst_prime, lst_not_prime, MAX):
    """
    (list,list,int)--->nothing
    For numbers in range from 1 to MAx modifies input lists:
    one list for prime numbers, another for not prime numbers
    """
    lst_prime.append(2)
    lst_not_prime.append(1)
    for iterator in range(2, MAX + 1):
        if pow(2, iterator, iterator) == 2:
            lst_prime.append(iterator)
        else:
            lst_not_prime.append(iterator)


def Lucky(lst_lucky, lst_not_lucky, MAX):
    """ (lst, lst, int) -> None
    Function genearte lst_lucky and lst_not_lucky
    """
    lst = [i for i in range(MAX + 1)]
    num = 1
    lst[0] = -1
    while(num < len(lst)):
        if num == 1:
            x = lst[num + 1]
        else:
            x = lst[num]
        for i in range(x, len(lst), x):
            lst_not_lucky.append(lst[i])
            lst[i] = False
        j = 1
        while (j < len(lst)):
            if lst[j] == False:
                lst.remove(lst[j])
            j += 1
        num += 1

    for i in lst:
        lst_lucky.append(i)


def isLucky(num):
    """
    (int)--> bool
    Returns True if num is lucky, else - False
    >>> isLucky(1)
    True
    """
    global lst_lucky
    return num in lst_lucky


def isPrime(num):
    """
    (int)--> bool
    Returns True if num is prime, else - False
    >>> isLucky(7)
    True
    """
    global lst_prime
    return num in lst_prime


def isUlam(number):
    """
    (int)--> bool
    Returns True if num is Ulam number, else - False
    >>> isLucky(3)
    True
    """
    global lst_ulam
    return number in lst_ulam


def GenNumbers(lst):
    """
    (list)-->list
    Generates sequence of random numbers from 1 to Max
    """
    import random
    numbers = []
    primes  = 0
    ulams = 0
    luckies = 0
    for i in lst:
        if i in lst_prime: primes += 1        
        if i in lst_lucky: luckies += 1
        if i in lst_ulam: ulams += 1
        numbers.append(i.num)
        
    if primes == 0:
        Choice = lst_prime
    elif ulams == 0:
        Choice = lst_ulam
    elif luckies == 0:
        Choice = lst_lucky
    else:
        Choise = random.choice([lst_not_prime, lst_not_lucky, lst_not_ulam])
    number = random.randrange(1, MAX)
    while number in numbers:
        number = random.choice(Choice)
    return number


Prime(lst_prime, lst_not_prime, MAX)
Lucky(lst_lucky, lst_not_lucky, MAX)
Ulam(lst_ulam, lst_not_ulam, MAX)
<<<<<<< HEAD:helper.py
print(lst_ulam)
=======
>>>>>>> d9c7a4b9e969a676297aade0fcd8cb2c910d80d7:valizzka_helper.py
