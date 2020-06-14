from collections import defaultdict

import yaml


class Vertex:
    def __init__(
        self,
        vertex_id,
        x=None,
        y=None,
        label=None,
    ):
        self.vertex_id = vertex_id
        self.x = x
        self.y = y
        self.label = label
        self.adjacent = []
        self.previous = None

    def __str__(self):
        return str(self.vertex_id)

    def __repr__(self):
        return self.__str__()


class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f"{self.v1} - {self.v2} ({self.weight})"

    def __repr__(self):
        return self.__str__()


class Partition:
    def __init__(self, elements):
        self.elements = sorted(list(map(int, elements)))

    def find_root(self, x):
        if x == self.elements[x]:
            return x
        while x != self.elements[x]:
            x = self.elements[x]
        return x

    def same_set(self, a, b):
        if self.find_root(a) == self.find_root(b):
            return True
        return False

    def same_set_and_union(self, a, b):
        a, b = int(a), int(b)
        if self.same_set(a, b):
            return True
        self.elements[self.find_root(a)] = self.find_root(b)
        return False


def read_yaml(file_name):
    vertices = set()
    edges = set()
    with open(file_name) as f:
        loaded = yaml.load(f, Loader=yaml.FullLoader)
    for v in loaded.get("vertices", []):
        vertices.add(Vertex(v))
    for e in loaded.get("edges", []):
        splitted = e.split(",")
        if len(splitted) == 2:
            edges.add(Edge(splitted[0], splitted[1]))
        elif len(splitted) == 3:
            edges.add(Edge(splitted[0], splitted[1], float(splitted[2])))
    return vertices, edges


def get_directed_adjacency_map(edges):
    """
    Return a directed adjacency map from an iterable storing edges.

    :param iterable[Edge] edges: set/list/etc of edges
    :return dict[list]: adjacency map
    """
    adj_map = defaultdict(list)
    for e in edges:
        adj_map[e.v1].append(e.v2)
    return adj_map


def get_undirected_adjacency_map(edges):
    """
    Return an undirected adjacency map from an iterable storing edges.

    :param iterable[Edge] edges: set/list/etc of edges
    :return dict[set]: adjacency map
    """
    adj_map = defaultdict(set)
    for e in edges:
        adj_map[e.v1].add(e.v2)
        adj_map[e.v2].add(e.v1)
    return adj_map


def get_undirected_adjacent(vertex_id, edges):
    """
    Get the list of vertices which are adjacent to a vertex.

    :param str vertex_id: ID of the vertex
    :param iterable[Edge]: set/list/etc of edges
    :return list[str]: list of adjacent vertices ID
    """
    adj_map = get_undirected_adjacency_map(edges)
    return adj_map.get(vertex_id, [])


def get_directed_adjacent(vertex_id, edges):
    """
    Get the list of vertices which are adjacent to a vertex.

    :param str vertex_id: ID of the vertex
    :param iterable[Edge]: set/list/etc of edges
    :return list[str]: list of adjacent vertices ID
    """
    adj_map = get_directed_adjacency_map(edges)
    return adj_map.get(vertex_id, [])


def dfs(edges, start, goal):
    """
    Finds a path within a graph using depth-first search.

    :param set[Edges] edges: edges of the graph
    :param str|int start: vertex ID of the starting point
    :param str|int goal: vertex ID of the goal
    :return Vertex: return the goal vertex if it was found
    """
    start = str(start)
    goal = str(goal)

    stack = []
    stack.append(Vertex(start))
    visited = set()
    visited.add(start)
    adj_map = get_directed_adjacency_map(edges)

    while stack:
        current = stack.pop()
        if current.vertex_id == goal:
            return current
        for adjacent in adj_map.get(current.vertex_id, []):
            if adjacent not in visited:
                vertex = Vertex(adjacent)
                vertex.previous = current
                stack.append(vertex)
                visited.add(adjacent)


def print_path(vertex):
    """
    Print the path which led to this vertex.

    :param Vertex vertex: vertex object
    """
    path = "end"
    while vertex:
        path = f"{vertex.vertex_id} -> " + path
        vertex = vertex.previous
    print(path)


def kruskal(edges):
    """
    Get the vertices which make a minimum spanning tree of the graph.
    The edges are assumed to be undirected.

    :param iterable[Edge] edges: edges of the graph
    :return list[Vertex]: vertices of a minimum spanning tree
    """
    spanning_tree = set()
    sorted_edges = sorted(edges, key=lambda x: x.weight)
    partition = Partition(sorted(get_vertices_from_edges(edges)))
    for edge in sorted_edges:
        if not partition.same_set_and_union(edge.v1, edge.v2):
            spanning_tree.add(edge)
    return spanning_tree


def get_vertices_from_edges(edges):
    """
    Get the vertices IDs from the edges of the graph.

    :param iterable[Edge] edges: edges of the graph
    :return list[int]: vertices IDs
    """
    vertices = set()
    for e in edges:
        vertices.add(e.v1)
        vertices.add(e.v2)
    return list(vertices)


if __name__ == "__main__":
    vertices, edges = read_yaml("graph2.yaml")
    path = dfs(edges, 0, 4)
    print_path(path)
