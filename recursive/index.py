# this is a simple case of a recursion algorithm. More sofisticated cases will be presented with quicksort 
# the algorithm involves sum an array of n elements without using loops

arr = [2,4,6]

def sum(x, i):
    if i < len(arr) - 1:
        sum(x, i + 1)
    return x + arr[i]