from Graph import *


def max_clique(graph: Graph):
    """
    An efficient algorithm for solving this problem is Bron Kerbosch's.
    We may use a real world analogy before actually heading to the implementation of this.
    Let's say we want to build a VIP club. Every person in this club must be friends
    with everyone else.
    current_clique is exactly that, the people standing inside the club.
    processed_vertices are people who have already thrown a party before. We keep track of them
    so that we don't hold the same party twice.
    candidates are people standing outside in a line, they are all friends with everyone inside
    the club.
    """
    cliques = []
    curr_clique = set()
    c = set(graph.get_vertices())
    proc_v = set()

    def bron_kerbosch(current_clique, processed_vertices, candidates, g: Graph):
        if not candidates and not processed_vertices:
            if len(current_clique) > 2:
                cliques.append(list(current_clique))
            return
        # we are taking everyone, both people who are waiting to get inside
        # and people who have already thrown a party.
        union_set = candidates.union(processed_vertices)
        # we want THE SOCIAL BUTTERFLY of the evening. The person who is
        # friends with most people.
        pivot = max(union_set, key=lambda x: len(g.neighbors(x)))
        # if we wouldn't do this, then we would start a party with a friend of the
        # social butterfly's and eventually the social butterfly himself would crash
        # the party.
        possibles = candidates.difference(g.neighbors(pivot))
        for v in possibles:
            # v enters the club. we create a brand new clipboard for it.
            # it contains everyone who was already in the club and v.
            new_clique = current_clique.union({v})
            # now that v is here, the rules of the club have changed a little.
            # we know that to be inside the club means to be friends with everyone already inside.
            # therefore, newcomers must be friends with v too.
            # Now through intersection, we are basically keeping in the waiting line
            # only people that are friends with v too.
            new_candidates = candidates.intersection(g.neighbors(v))
            # let's say that vertex Alex knows v, but Alex has already hosted a party.
            # without this, we are threatened to have Alex throw a duplicate party.
            # Basically, anyone who knows v and has already been processed isn't
            # allowed to crash the party. People who don't know v can't crash it anyway.
            new_processed_vertices = processed_vertices.intersection(g.neighbors(v))
            bron_kerbosch(new_clique, new_processed_vertices, new_candidates, g)
            # once we found all maximal cliques that include v, we are done with it.
            # we've explored all its possibilities, so we remove and process him.
            candidates.remove(v)
            processed_vertices.add(v)

    bron_kerbosch(curr_clique, proc_v, c, graph)
