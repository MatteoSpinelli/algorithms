import copy
from collections import deque

""" 
this in an implementation of the breadth first search algorithm, wich is capable of find if an object is inside a graph (hash map) and what is the shortest path
beetween the starting point of the graph and the object

here there is a simple graph, the purpose of the algorithm is to find, if exist, the nearest name wich ends with the letter m
 """

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def validate_function(name: str):
    # this function decide whether or not the item is a correct match
    if name[-1] == "w":
        return True
    return False


def breadth_first_search(graph: dict[list], validate, startingPoint="you"):
    """
    This is the actual implementation of the algorithm: \n
    The algoritm iterates over a queue and for every object wich not corresponds to the search criteria it adds its connected objects. \n
    Also it store a list cointains the objects already searched.
    """
    queue = deque(graph[startingPoint])
    n_steps = 1
    searched = []
    while queue:
        searchLen = len(queue)
        for _ in range(searchLen):
            node = queue.popleft()
            if validate(node):
                return node, n_steps
            queue += graph[node]
            searched.append(node)
        n_steps += 1
    return False

breadth_first_search(graph, validate_function)