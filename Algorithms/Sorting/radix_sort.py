import sys
import random
import string

def LSD_radix_sort(arr):
    length = None
    for s in arr:
        if length == None:
            length = len(s)
        assert length == len(s)
    r = 256
    n = len(arr)
    aux = [0] * n

    for letter in range(len(arr[0]) - 1, -1, -1):
        count = [0] * r
        #Count number of each item
        for i in range(n):
            count[ord(arr[i][letter])+1] += 1

        #Turn counts into indices
        for i in range(1, r):
            count[i] += count[i - 1]

        #Use indices to insert into aux
        for i in range(n):
            aux[count[ord(arr[i][letter])]] = arr[i]
            count[ord(arr[i][letter])] += 1

        #Copy from aux to original
        for i in range(n):
            arr[i] = aux[i]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        arr = []
        for x in range(100):
            arr.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100)))
        LSD_radix_sort(arr)
        for i in arr:
            print i
    else:
        arr = sys.argv[1::]
        LSD_radix_sort(arr)
        for s in arr:
            print s
