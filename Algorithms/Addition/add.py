import os
import sys

'''
Input: Two integers
Output: A string of the sum of the inputs
'''
def add(x, y):
    carry = 0
    #Convert x and y from integers to '0' padded arrays of integers
    #Example: 1 + 123 becomes [0, 0, 1] + [1, 2, 3]
    n = max(len(str(x)), len(str(y)))
    x = map(int, "%0*d" % (n, x))
    y = map(int, "%0*d" % (n, y))
    result = ""
    for i in range(1, n + 1):
        dsum = x[n - i] + y[n - i]
        if carry == 0:
            if dsum < 9:
                result = str(dsum) + result
                carry = 0
            else:
                result = str(dsum % 10) + result
                carry = dsum / 10
        else:
            if dsum + carry < 9:
                result = str(dsum + carry) + result
                carry = 0
            else:
                result = str((dsum + carry) % 10) + result
                carry = (dsum + carry) / 10
    if carry:
        result = str(carry) + result
    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Invalid number of args"
    else:
        print add(int(sys.argv[1]), int(sys.argv[2]))
