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
    if number < 1:
        return False
    elif number < 3:
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


def isLucky(number):
    """
    (int>0)-->bool
    Given positive integer returns True if int is lucky, else returns False
    >>> isLucky(13)
    True
    >>> isLucky(2)
    False
    >>> isLucky(7)
    True
    """
    List = range(-1, number*number+9, 2)
    i = 2
    while List[i:]:
        List = sorted(set(List)-set(List[List[i]::List[i]]))
        i += 1
    return number in List
    # l = range(1, number + 1, 2)
    # i = 1
    # while i < len(l):
    #     del(l[l[i] - 1::l[i]])
    #     i += 1
    # return l


def GenNumbers(lst):
    import random
    numbers = []
    for i in lst:
        numbers.append(i.num)
    number = random.randrange(1, 100)
    while number in numbers:
        number = random.randrange(1, 100)
    return number
print(isPrime(72))
