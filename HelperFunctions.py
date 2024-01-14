import math, time

def listPrimes(upperBound):
    primeField = [True for i in range(upperBound+1)]
    #print(primeField)
    p=2
    while (p**2 <= upperBound):
        if (primeField[p]):
            for i in range(p**2, upperBound+1, p):
                primeField[i] = False
        p += 1
    #print(primeField)
    primes = []
    for j in range(2, upperBound+1):
        if primeField[j]:
            #print(j)
            #print(primes)
            primes.append(j)
            #print(primes)
    #print(primes)
    return primes

def boolPrimes(upperBound):
    primeField = [True for i in range(upperBound+1)]
    #print(primeField)
    p=2
    while (p**2 <= upperBound):
        if (primeField[p]):
            for i in range(p**2, upperBound+1, p):
                primeField[i] = False
        p += 1
    return primeField

def isPrime(n):
    #"""
    #Set of all natural numbers
    if n==1 or n==0: #Remove 0 and 1 as False
        return False
    elif n<4: #Remove 2 and 3 as True
        return True
    elif n%2 == 0: #Remove all other even numbers as False
        return False
    elif n<9: #Remove the remaining less than 9: 5 and 7 as True
        return True
    elif n%3 == 0: #Remove all other multiples of 3 as False
        return False
    else:
        limit = math.floor(math.sqrt(n)) #largest possible first factor of a number
        f=6 #Will be incremented by 6 because of 6k+1 and 6k-1
        while f-1<=limit:
            if n%(f-1) == 0: #6k-1
                return False
            if n%(f+1) == 0:
                return False
            f += 6
        return True #If all conditions are met than it is prime
            
    #Improvements based on Problem 7 printed solution
    """
    if n%2 == 0:
        return False
    elif (n+1)%6 != 0 and (n-1)%6 != 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(n)+1), 2):
            if n%i == 0:
                return False
        return True
    """
#for i in range(1, 25):
#    print(i, isPrime(i))

def sumDivisors(n):
    total = 0

    for i in range(1, int(math.floor(math.sqrt(n)))+1):
        if n%i == 0:
            total += i + n/i

    if math.sqrt(n)%1 == 0:
        total -= int(math.sqrt(n))

    return total - n

def generateNextFibbSection(fibbSection):
    fibbSection[0] = fibbSection[1]
    fibbSection[1] = fibbSection[2]
    fibbSection[2] = fibbSection[0] + fibbSection[1]
    return fibbSection

def getDivisors(n):
    divisors = []

    for i in range(1, int(math.floor(math.sqrt(n)))+1):
        if n%i == 0:
            divisors.append(i)

    return divisors

def isPalindromeString(string):
    return string == string[::-1]

def getPrimeFactors(n):
    workingN = n
    pFactors = []
    timesDivided = 0
    while workingN % 2 == 0:
        workingN /= 2
        timesDivided += 1
    if timesDivided > 0:
        pFactors.append((2,timesDivided))
    for p in range(3, int(math.ceil(math.sqrt(workingN)))):
        timesDivided = 0
        if (workingN % p == 0):
            while (workingN % p == 0):
                workingN /= p
                timesDivided += 1
            pFactors.append((p, timesDivided))
    if (workingN > 2):
        pFactors.append((int(workingN), 1))
    return pFactors
