import sys

def bubble_sort(arr):
    solved = False
    while not solved:
        solved = True
        for x in range(1, len(arr)):
            if arr[x - 1] > arr[x]:
                arr[x - 1], arr[x] = arr[x], arr[x - 1]
                solved = False
                print arr
    print arr

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Invalid number of args"
    else:
        bubble_sort(map(int, sys.argv[1::]))
