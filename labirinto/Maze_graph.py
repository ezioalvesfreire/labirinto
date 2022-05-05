class Node:
    # black -> finalizado
    # white -> não visitado
    # gray  -> percorrido (aguardando visita)

    def __init__(self, line, column, value):
        self.line = line
        self.column = column
        self.value = value
        self.not_visited()

    def visit(self):
        self.color = 'black'

    def not_visited(self):
        self.color = 'white'

    #foi visitado
    def is_visited(self):
        return self.color == 'black'

    #augardando visita
    def is_waiting(self):
        return self.color == 'gray'

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        self.m_list_of_edges = []

    def add_edge(self, node1, node2, weight=1):
        # Add the edge from node1 to node2
        self.m_list_of_edges.append([node1, node2, weight])

        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
            self.m_list_of_edges.append([node1, node2, weight])

    # Print a graph representation
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i + 1, ": ", self.m_list_of_edges[i])