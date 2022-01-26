
# Reads a file that has the text.

def textparser(file):
        with open(file) as k:
            s = ""
            for i in k:
                s = s + i
        return s

# Used to find the a base raised to a power, then modulo applied in log time with respect to the power. This uses
# properties of modulo to develop cases on whether the input power is odd or even.

def modexponenthelper(power, base, modulo):
    if base == 0:
        return 0
    if power == 0:
        return 1
    if power % 2 == 0:
        return (modexponenthelper(power/2, base, modulo) * modexponenthelper(power/2, base, modulo)) % modulo
    else:
        return ((modexponenthelper(power-1, base, modulo) % modulo) * (base % modulo)) % modulo

# Uses Horner's Method to calculate the initial hashes without causing integer overflows

def initializehash(substring, m, a):
    patternhash = 0
    temp = len(substring)
    for i in substring:
        patternhash = ((patternhash * a) + ord(i)) % m # initializes the hash value of pattern
        temp -= 1
    return patternhash

# Calculates the hash code for the next subseqeunce that has the length of the pattern using the previous hash code
# value

def recalculatehash(oldhash, oldchar, newchar, m, a, a1):
    newhash = ((((oldhash - (ord(oldchar) % m * a1) % m) * a) % m) + ord(newchar)) % m # The +m is just to make sure we don't have a negative
    return newhash


# Takes a file with the text, a list of all the patterns, a modulo value, and a multiplier (base) value. Outputs
# The location of where the pattern is located in the text if it is found.

def rabin_karp(file, patternset, modulo , multiplier):
    text = textparser(file)
    hashestopatterns = {}
    for i in patternset:
        phash = initializehash(i, modulo, multiplier)
        hashestopatterns[phash] = i

    # Pre-Processed Multiplier
    ppm = modexponenthelper(len(patternset[0]) - 1, multiplier, modulo)

    n = len(text)
    m = len(patternset[0])
    subhash = initializehash(text[0:m], modulo, multiplier)
    for i in range(0, n-m + 1):
        if hashestopatterns.__contains__(subhash):
            curr = text[i:i + m]
            if hashestopatterns[subhash].__eq__(curr):
                print(hashestopatterns[subhash] + " found at index " + str(i))
        if i == n-m:
            break
        subhash = recalculatehash(subhash, text[i], text[i + m], modulo, multiplier, ppm)
