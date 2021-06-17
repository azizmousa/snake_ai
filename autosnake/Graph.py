from Node import Node
from Connection import Connection

"""
graph = {node1: [(node2, weight1), (node3, weight2), (node4, weight3)]}
graph = {node1: [connection1, connection2, connection3]}
"""


class Graph:
    def __init__(self):
        self.__graph = {}

    def set_node(self, node_x, node_y):
        node = Node(node_x, node_y)
        if node not in self.__graph:
            self.__graph[node] = []
        return node

    def add_connection(self, node_x, node_y, connection_x, connection_y, weight):
        node = self.set_node(node_x, node_y)
        connection = Connection(Node(connection_x, connection_y), weight)
        self.__graph[node].append(connection)

    def get_graph(self):
        return self.__graph

    def get_node_connections(self, node_x, node_y):
        node = Node(node_x, node_y)
        if node in self.__graph:
            return self.__graph[node]
        return None
