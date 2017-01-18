import sys

def merge(arr, low, mid, high, aux):
    assert sorted(arr[low:mid]) == arr[low:mid]
    assert sorted(arr[mid+1:high+1]) == arr[mid+1:high+1]
    for i in range(low, high + 1):
        aux[i] = arr[i]
    left = low
    right = mid + 1
    for i in range(low, high + 1):
        if left > mid:
            arr[i] = aux[right]
            right += 1
        elif right > high:
            arr[i] = aux[left]
            left += 1
        elif aux[left] < aux[right]:
            arr[i] = aux[left]
            left += 1
        else:
            arr[i] = aux[right]
            right += 1
    print arr

def recursive_sort(arr, low, high, aux):
    if low >= high:
        return
    mid = low + (high - low) / 2
    recursive_sort(arr, low, mid, aux)
    recursive_sort(arr, mid + 1, high, aux)
    merge(arr, low, mid, high, aux)


def recursive_merge_sort(arr):
    aux = arr[:]
    recursive_sort(arr, 0, len(arr) - 1, aux)

def bottom_up_merge_sort(arr):
    aux = list(arr)
    n = 1
    a = len(arr)
    while n < a:
        lo = 0
        while lo < a - n:
            merge(arr, lo, lo + n - 1, min(a - 1, lo + n*2-1), aux)
            lo += n * 2
        n *= 2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Invalid number of args"
    else:
        bottom_up_merge_sort(map(int, sys.argv[1::]))
