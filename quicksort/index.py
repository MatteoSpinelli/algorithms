# quicksort is an algorithn much faster than the selection sort algorithm
# base cases:
# array of size 0 or 1 are pretty easy to sort:
# if an array has size 0 ([]) or size 1 ([20]) return the array
# if an array has size 2, like [17, 10], just check if the first element is greater than the second, if so, swap the elements
# recursive case:
# select a pivot, divide the list in two list, one greter and one smaller than the pivot.
# then call the quicksort on both the lists

import random

arr = [1,1,1,1,4,4,4,4,2,2,2,5,5,5]
random.shuffle(arr)

def quicksort(list):
    # implement the quicksort algorithm, with a random pivot
    if len(list) < 2:
        return list
    if len(list) == 2:
        if list[0] > list[1]:
            return [list[1], list[0]]
        return list
    # recurive case
    pivot = random.choice(list)
    sub_list = [i for i in list if i <= pivot]
    sub_list.remove(pivot)
    sup_list = [i for i in list if i > pivot]
    return quicksort(sub_list) + [pivot] + quicksort(sup_list)




