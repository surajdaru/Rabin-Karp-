# Everything in this file is essentially the same as the rabin_karp.py file, however the output for rabin_karp here
# are just print statements of what patterns were not found in the input text.

def textparser(file):
    with open(file) as k:
        s = ""
        for i in k:
            s = s + i.strip()
    return s

def modexponenthelper(power, base, modulo):
    if base == 0:
        return 0
    if power == 0:
        return 1
    if power % 2 == 0:
        return (modexponenthelper(power/2, base, modulo) * modexponenthelper(power/2, base, modulo)) % modulo
    else:
        return ((modexponenthelper(power-1, base, modulo) % modulo) * (base % modulo)) % modulo

def initializehash(substring, m, a):
    patternhash = 0
    temp = len(substring)
    for i in substring:
        patternhash = ((patternhash * a) + ord(i)) % m
        temp -= 1
    return patternhash

def recalculatehash(oldhash, oldchar, newchar, m, a, ppm):
    newhash = ((((oldhash - (ord(oldchar) % m * ppm) % m) * a) % m) + ord(newchar)) % m
    return newhash


def rabin_karp(file, patternset, modulo, multiplier):
    text = textparser(file)
    hashestopatterns = {}
    foundpatterns = []
    for i in patternset:
        phash = initializehash(i, modulo, multiplier)
        hashestopatterns[phash] = i

    # Pre-Processed Multiplier
    ppm = modexponenthelper(len(patternset[0]) - 1, multiplier, modulo)

    n = len(text)
    m = len(patternset[0])
    subhash = initializehash(text[0:m], modulo, multiplier)
    for i in range(0, n - m + 1):
        if hashestopatterns.__contains__(subhash):
            curr = text[i:i + m]
            if hashestopatterns[subhash].__eq__(curr):
                foundpatterns.append(curr)
        if i == n - m:
            break
        subhash = recalculatehash(subhash, text[i], text[i + m], modulo, multiplier, ppm)
    for i in patternset:
        if not foundpatterns.__contains__(i):
            print(i + " NOT FOUND")