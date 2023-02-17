# implementantion of the binary search algorithm

arr = [i for i in range(100)]

def binary_search(sortedArray, n):
    low = 0
    high = len(sortedArray) - 1
    while True:
        print(low, high)
        delta = (high - low) / 2
        mid = round(delta + low)
        if n > sortedArray[mid]:
            low = mid
        elif n < sortedArray[mid]:
            high = mid
        else:
            return mid
            


