import sys
from random import shuffle

def parition(arr, low, high):
    i = low + 1
    j = high
    while True:
        while (arr[i] < arr[low]):
            if i == high:
                break
            i += 1
        while (arr[low] < arr[j]):
            if j == low:
                break
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    # print arr
    return j

def sort(arr, low, high):
    if low >= high:
        return
    j = parition(arr, low, high)
    sort(arr, low, j - 1)
    sort(arr, j + 1, high)

def quick_sort(arr):
    shuffle(arr)
    sort(arr, 0, len(arr) - 1)
    # print arr

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Invalid number of args"
    else:
        quick_sort(map(int, sys.argv[1::]))
