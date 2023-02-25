# selection sort algorithm, complexity: O(n^2)
arr = [12,6,19,100,1,0,240,758,-12,-345]

# the operations are these:
# 1. find the smallest value in the array
# 2. append that value to the result array
# 3. delete the element from the array
# 4. repeat for every element of the array

def findSmallestValue(arr):
    # return the index and the element of the smallest element of the array
    min = None
    indexMin = 0
    for i, el in enumerate(arr):
        if min == None or el < min:
            min = el
            indexMin = i
    return indexMin

def selection_sort(arr: list):
    # return the sorted array
    res = []
    for _ in range(len(arr)):
        indexMin = findSmallestValue(arr)
        res.append(arr.pop(indexMin))
    return res


