# this is the first implementation of the dijkstra's algorithm to find the shortest path in a weighted graph
# it works with two steps:
#   1. from the starting node, find the cheapest neighbour node
#   2. figure out what it the cost to go from the cheapest node to its neighbour
#   repeat

import numpy as np

graph = {
    "book": [["lp", 5], ["poster", 0]],
    "lp": [["guitar", 15], ["drums", 20]],
    "poster": [["guitar", 30], ["drums", 35]],
    "guitar": [["piano", 20]],
    "drums": [["piano", 10]],
    "piano": [],
}

nc = {
    "lp": np.inf,
    "poster": np.inf,
    "guitar": np.inf,
    "drums": np.inf,
    "piano": np.inf,
}

parents = {
    "lp": "book",
    "poster": "book",
    "guitar": "",
    "drums": "",
    "piano": "",
}

def main():
    for node in graph.keys():
        weights = graph[node]
        if len(weights) == 0:
            break
        for w in weights:
            if node == "book":
                nc[w[0]] = w[1]
                continue
            updatedCost = w[1] + nc[node]
            if updatedCost < nc[w[0]]:
                nc[w[0]] = updatedCost
                parents[w[0]] = node
    
    path = ["piano"]
    target = "piano"
    while target != "book":
        for key, value in parents.items():
            if key == target:
                path.append(value)
                target = value
    return path