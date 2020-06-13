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


class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


def read_yaml(file_name):
    vertices = set()
    edges = set()
    with open(file_name) as f:
        loaded = yaml.load(f, Loader=yaml.FullLoader)
    for v in loaded.get("vertices", []):
        vertices.add(Vertex(v))
    for e in loaded.get("edges", []):
        head, tail = e.split(",")
        edges.add(Edge(head, tail))
    return vertices, edges


def get_adjacency_map(edges):
    """
    Return an adjacency map from an iterable storing edges.

    :param iterable[Edge] edges: set/list/etc of edges
    :return dict[list]: adjacency map
    """
    adj_map = defaultdict(list)
    for e in edges:
        adj_map[e.v1].append(e.v2)
    return adj_map


def get_adjacent(vertex_id, edges):
    """
    Get the list of vertices which are adjacent to a vertex.

    :param str vertex_id: ID of the vertex
    :param iterable[Edge]: set/list/etc of edges
    :return list[str]: list of adjacent vertices ID
    """
    adj_map = get_adjacency_map(edges)
    return adj_map.get(vertex_id, [])


def dfs(edges, start, goal):
    """
    Finds a path within a graph using depth-first search.

    :param set[Edges] edges: edges of the graph
    :param str start: vertex ID of the starting point
    :param str goal: vertex ID of the goal
    :return Vertex: return the goal vertex if it was found
    """
    stack = []
    stack.append(Vertex(start))
    visited = set()
    visited.add(start)

    while stack:
        current = stack.pop()
        if current.vertex_id == goal:
            return current
        for adjacent in get_adjacent(current.vertex_id, edges):
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


if __name__ == "__main__":
    vertices, edges = read_yaml("graph1.yaml")
    path = dfs(edges, "2", "7")
    print_path(path)
