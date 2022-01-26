This is the code implementation of the Rabin-Karp algorithm, part of a final project I completed CSCI 1810 at
Brown University.

rabin_karp.py implements the string-searching algorithm with the use of hashcodes. Each subtring gets its own hashcode
and is compared to that of the input pattern. If a match is found, it is printed out. The rolling hash implementation
makes sure that we can get each subsequent hashcode in constant time. The use of modulo is to prevent integer overflow errors.

application.py performs the same as rabin_karp.py, except that it is only prints when a match is not found. This is because
I was applying it to a particular protein subunit to figure out the % conservation of certain subsequences. 