from Graph import *


def chromatic_number(graph: Graph):
    colours = {}
    vertices = graph.get_vertices()
    sorted_vertices = []

    for vertex in vertices:
        colours[vertex] = -1
        sorted_vertices.append(vertex)

    sorted_vertices.sort(key=lambda v: len(graph.neighbors(v)), reverse=True)
    for vertex in sorted_vertices:
        used_colours = set()
        for neighbour in graph.neighbors(vertex):
            if colours[neighbour] != -1:
                used_colours.add(colours[neighbour])
        colour_to_assign = 1
        while colour_to_assign in used_colours:
            colour_to_assign += 1
        colours[vertex] = colour_to_assign

    cn = max(colours.values())
    return cn
