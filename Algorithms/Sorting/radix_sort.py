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

    for letter in range(length - 1, -1, -1):
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


def MSD_radix_sort(arr, aux, lo, hi, d):
    if hi <= lo:
        return
    r = 256

    count = [0] * (r + 2)
    #Count number of each item
    for i in range(lo, hi):
        if d < len(arr[i]):
            count[ord(arr[i][d])+1] += 1

    #Turn counts into indices
    for i in range(1, r + 1):
        count[i] += count[i - 1]

    #Use indices to insert into aux
    for i in range(lo, hi):
        if d < len(arr[i]):
            aux[count[ord(arr[i][d])]] = arr[i]
            count[ord(arr[i][d])] += 1

    #Copy from aux to original
    for i in range(lo, hi):
        arr[i] = aux[i]

    for i in range(r):
        MSD_radix_sort(arr, aux, lo + count[r], lo + count[r + 1] - 1, d + 1)

def MSD(arr):
    aux = [0] * len(arr)
    MSD_radix_sort(arr, aux, 0, len(arr), 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        arr = []
        for x in range(100):
            arr.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        MSD(arr)
        for i in arr:
            print i
    else:
        arr = sys.argv[1::]
        MSD(arr)
        for s in arr:
            print s

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         arr = []
#         for x in range(100):
#             arr.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100)))
#         LSD_radix_sort(arr)
#         for i in arr:
#             print i
#     else:
#         arr = sys.argv[1::]
#         LSD_radix_sort(arr)
#         for s in arr:
#             print s
