from Node import Node
from Connection import Connection

"""
graph = {node1: [(node2, weight1), (node3, weight2), (node4, weight3)]}
graph = {node1: [connection1, connection2, connection3]}
"""


class Graph:
    def __init__(self, cols, rows, step):
        self.__graph = {}
        self.__rows = rows // step
        self.__cols = cols // step
        self.__step = step

    def __create_node(self, node_x, node_y):
        node = Node(node_x, node_y)
        if node not in self.__graph:
            self.__graph[node] = []
        return node

    def insert_node(self, node_x, node_y, initiate=False):
        if not initiate:
            node_x = node_x // self.__step
        if not initiate:
            node_y = node_y // self.__step
        node = Node(node_x, node_y)
        if node not in self.__graph:
            self.__graph[node] = []

        left_node = Node(node.get_x() - 1, node.get_y())
        right_node = Node(node.get_x() + 1, node.get_y())
        above_node = Node(node.get_x(), node.get_y() - 1)
        below_node = Node(node.get_x(), node.get_y() + 1)
        self.__add_connection(node, left_node, 1)
        self.__add_connection(node, right_node, 1)
        self.__add_connection(node, above_node, 1)
        self.__add_connection(node, below_node, 1)
        self.__add_connection(left_node, node, 1)
        self.__add_connection(right_node, node, 1)
        self.__add_connection(above_node, node, 1)
        self.__add_connection(below_node, node, 1)
        return node

    def initiate_graph(self):
        for y in range(self.__rows):
            for x in range(self.__cols):
                self.__create_node(x, y)

        for node in self.__graph:
            self.insert_node(node.get_x(), node.get_y(), True)

    def remove_node(self, x, y):
        x = x//self.__step
        y = y//self.__step
        node = Node(x, y)
        if node in self.__graph:
            left_node = Node(x - 1, y)
            right_node = Node(x + 1, y)
            above_node = Node(x, y - 1)
            below_node = Node(x, y + 1)
            self.__remove_connection(node, left_node, 1)
            self.__remove_connection(node, right_node, 1)
            self.__remove_connection(node, above_node, 1)
            self.__remove_connection(node, below_node, 1)
            del self.__graph[node]

    def __add_connection(self, node, target, weight):
        if node in self.__graph and target in self.__graph:
            connection1 = Connection(target, weight)
            if connection1 not in self.__graph[node]:
                self.__graph[node].append(connection1)

    def __remove_connection(self, node1, node2, weight):
        if node2 in self.__graph:
            connection = Connection(node1, weight)
            self.__graph[node2].remove(connection)

    def get_graph(self):
        return self.__graph

    def get_graph_size(self):
        return len(self.__graph)

    def get_node_connections(self, node_x, node_y):
        node = Node(node_x, node_y)
        if node in self.__graph:
            return self.__graph[node]
        return None

    def __str__(self):
        return str(self.__graph)
