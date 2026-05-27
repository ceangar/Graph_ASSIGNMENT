#A dominating set of an undirected graph is a set of vertices D such that every vertex in the graph is either:
#-inside D
#-adjacent to at least one vertex in D
#A minimum dominating set is a dominating set with the smallest possible size.

#SOLUTION:
#To find all minimum dominating sets, we can try all subsets of vertices, starting from size 1, then size 2, then size 3, etc.
#The first time we find at least one dominating set of size k, we stop, because all larger sets are not minimum anymore.

from itertools import combinations


from itertools import combinations
#combinations function from itertools can be used instead of the function below
#I just wanted to implement my own combinations function :D

def my_combinations(elements, size):
    result = []

    def backtrack(start_index, current_combination):
        # If we reached the desired size, save this combination
        if len(current_combination) == size:
            result.append(current_combination.copy())
            return

        # Try adding each possible next element
        for i in range(start_index, len(elements)):
            current_combination.append(elements[i])

            # Continue after i, not from 0, to avoid duplicates
            backtrack(i + 1, current_combination)

            # Remove the last element and try another one
            current_combination.pop()

    backtrack(0, [])

    return result


def is_dominating_set(graph, candidate):
    dominated = set()

    #every vertex must be either in D or adjacent to a vertex in D
    for vertex in candidate:
        dominated.add(vertex)
        dominated.update(graph.neighbors(vertex))

    return dominated == set(graph.get_vertices())


def find_all_minimum_dominating_sets(graph):
    vertices = graph.get_vertices()

    #we start with sizes in increasing order(we are looking for the minimum dominating set)
    for size in range(1, graph.get_v() + 1): #size is between 1 and graph.get_v()
        result = []

        for subset in combinations(vertices, size):#we try all combinations of size vertices
            if is_dominating_set(graph, subset):
                result.append(set(subset))

        if result:#first result is the correct one since size is increasing with every iteration
            return result

    return [] #this will actually never happen since every non-empty graph has a dominating set
    #its just a convention for if our graph is empty, so that the function returns something everytime