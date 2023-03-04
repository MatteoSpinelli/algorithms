# this is a simple case of a recursion algorithm. More sofisticated cases will be presented with quicksort 
# the algorithm involves sum an array of n elements without using loops
"""
list = [] return 0
list = [3] return 3
list = [2,3] return 5
list = [1,2,3] return 6
"""

arr = [i for i in range(1, 101)]

def sum(list):
    if list == []:
        return 0
    return sum(list[1:]) + list[0]


"""
list = [] return 0
list = [3] return 1
list = [2,3] return 2
list = [1,2,3] return 3
"""


def countItems(list):
    # count the elements of a list
    if list == []:
        return 0
    return countItems(list[1:]) + 1


"""
list = [] return 0
list = [3] if 0 > 3 return 0 else 3 (return 3)
list = [2,3] if 3 > 2 return 3 else 2 (return 3)
list = [1,2,3] if 3 > 1 return 3 else 1
"""

def findMax(list):
    # return the maximum element in a list
    if list == []:
        return 0
    el = findMax(list[1:])
    if el > list[0]:
        return el
    return list[0]



    