#!/usr/bin/env python3

from math import factorial


def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i               # shorthand for `fact = fact * i`
    return fact


def recursive_factorial(n):
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n-1)
        temp = temp * n
    return temp


def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)


def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) -1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp


if __name__ == '__main__':
    print(iterative_factorial(5))  # should be 120
    # 1 x 2 = 2, 2 x 3 = 6, 6 x 4 = 24, 24 x 5 = 120

    print(recursive_factorial(6))

    print(permute("AB", ""))

    s = 'abc'
    s = list(s)
    permutations(s)
