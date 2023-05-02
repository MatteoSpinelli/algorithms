# this is the first implementation of the dijkstra's algorithm to find the shortest path in a weighted graph
# it works with two steps:
#   1. from the starting node, find the cheapest neighbour node
#   2. figure out what it the cost to go from the cheapest node to its neighbour
#   repeat

graph = {
    "start": { "A": 6, "B": 2 },
    "A": { "FIN": 1 },
    "B": { "A": 3, "FIN": 5 },
    "FIN": {}
}

costs = {}

parents = {}

def find_cheapest(start):
    pass
        

def update_cost():
    pass

def update_parent():
    pass

def dijkstra_algo():
    pass

if __name__ == "__main__":
    dijkstra_algo()