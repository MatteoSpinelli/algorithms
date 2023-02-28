# this is a simple case of a recursion algorithm. More sofisticated cases will be presented with quicksort 
# the algorithm involves sum an array of n elements without using loops
"""
i=2 return 6
i=1 return 10
i=0 return 12
"""

arr = [i for i in range(1, 101)]

def sum(i):
    if i == len(arr) - 1:
        return arr[i]
    return arr[i] + sum(i + 1)

    