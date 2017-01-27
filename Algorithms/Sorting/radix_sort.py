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
            # print arr[i]
        # print ""

def MSD_radix_sort(arr, aux, lo, hi, d):
    if hi <= lo:
        return
    r = 256

    count = [0] * (r + 2)
    #Count number of each item
    for i in range(lo, hi + 1):
        if i < len(arr):
            if d < len(arr[i]):
                count[ord(arr[i][d])+2] += 1
            else:
                count[1] += 1

    #Turn counts into indices
    for i in range(1, r + 1):
        count[i] += count[i - 1]

    #Use indices to insert into aux
    for i in range(lo, hi + 1):
        if i < len(arr):
            if d < len(arr[i]):
                aux[count[ord(arr[i][d]) + 1]] = arr[i]
                count[ord(arr[i][d]) + 1] += 1
            else:
                aux[count[0]] = arr[i]
                count[0] += 1

    #Copy from aux to original
    for i in range(lo, hi + 1):
        if i < len(arr):
            arr[i] = aux[i - lo]

    for i in range(r):
        MSD_radix_sort(arr, aux, lo + count[i], lo + count[i + 1] - 1, d + 1)

def MSD(arr):
    aux = [0] * len(arr)
    MSD_radix_sort(arr, aux, 0, len(arr), 0)


def three_way_sort(arr, lo, hi, d):
    if hi <= lo:
        return
    lt = lo
    gt = hi
    if d >= len(arr[0]):
        v = -1
    else:
        v = arr[lo][d]
    i = lo + 1

    while i < gt:
        if d >= len(arr[0]):
            t = -1
        else:
            t = arr[i][d]
        if t < v:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif t > v:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    three_way_sort(arr, lo, lt - 1, d)
    if v >= 0:
        three_way_sort(arr, lt, gt, d + 1)
    three_way_sort(arr, gt + 1, hi, d)

def three_way(arr):
    three_way_sort(arr, 0, len(arr) - 1, 0)

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         arr = []
#         for x in range(10000):
#             arr.append(''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(64)))
#         three_way(arr)
#         for i in arr:
#             print i
#     else:
#         arr = sys.argv[1::]
#         three_way(arr)
#         for s in arr:
#             print s

if __name__ == "__main__":
    if len(sys.argv) < 2:
        arr = []
        for x in range(10000):
            arr.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)))
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
#         for x in range(10000):
#             arr.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)))
#             # print arr[x]
#         # print ""
#         LSD_radix_sort(arr)
#         for i in arr:
#             print i
#     else:
#         arr = sys.argv[1::]
#         LSD_radix_sort(arr)
#         for s in arr:
#             print s
