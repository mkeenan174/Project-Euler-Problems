
def findPalindrone():
    for a in range(900,999):
        for b in range(900,999):
            palindrone = a * b
            largestPalindrone = 0
            s = str(palindrone)
            rev = s[::-1]
            if s == rev and int(s) > largestPalindrone :
                largestPalindrone = s
                print(largestPalindrone)
        



findPalindrone()
