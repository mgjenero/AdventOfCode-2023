from networkx import Graph, minimum_edge_cut, connected_components


def size_of_groups(lines):
    nodes = set()
    edges = set()
    for line in lines:
        node, connection_nodes = line.split(": ")
        nodes.add(node)
        for connection_node in connection_nodes.split():
            nodes.add(connection_node)
            edges.add(tuple(sorted([node, connection_node])))
    graph = Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    # find min-cut of graph(we know min cut is 3)
    min_cut = minimum_edge_cut(graph)
    for edge in min_cut:
        graph.remove_edge(*edge)

    # find size of each connected components  and calculate result
    parts = connected_components(graph)
    res = 1
    for part in parts:
        res *= len(part)
    return res


# Testing
test1 = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""
ans1 = 54
assert size_of_groups(test1.splitlines()) == ans1

# Read input
with open('day25.txt') as f:
    input = f.read().splitlines()
    print(size_of_groups(input))
