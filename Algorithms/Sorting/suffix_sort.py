import sys
from quick_sort import quick_sort

#Naive implementation
def suffix_sort(s):
    arr = []
    for i in range(len(s)):
        arr.append(s[i::])
    quick_sort(arr)
    return arr

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Invalid number of args"
    else:
        arr = suffix_sort(sys.argv[1])
        for substring in arr:
            print substring
