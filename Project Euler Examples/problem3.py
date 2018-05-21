from symbol import factor

def findFactors(num):
    factors = []
    for factor in range(1, num + 1 ):
        if num % factor == 0:
            factors.append(factor)
            
    return factors
    



def primeChecker(num):
    return len(findFactors(num)) == 2
    factorList = findFactors(12)
    bigPrime = 0
    for factor in factorList:
        if primeChecker(factor) and factor > bigPrime:
            factor = bigPrime
            
    print (bigPrime) 