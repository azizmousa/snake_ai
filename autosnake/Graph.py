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

    def create_node(self, node_x, node_y):
        node = Node(node_x, node_y)
        if node not in self.__graph:
            self.__graph[node] = []
        print(node, "added")
        return node

    def insert_node(self, node_x, node_y):
        node = Node(node_x, node_y)
        if node not in self.__graph:
            self.__graph[node] = []
        left_node = Node(node.get_x() - self.__step, node.get_y())
        right_node = Node(node.get_x() + self.__step, node.get_y())
        above_node = Node(node.get_x(), node.get_y() - self.__step)
        below_node = Node(node.get_x(), node.get_y() + self.__step)
        self.__add_connection(node, left_node, 1)
        self.__add_connection(node, right_node, 1)
        self.__add_connection(node, above_node, 1)
        self.__add_connection(node, below_node, 1)
        print(node, "inserted")
        return node

    def initiate_graph(self):
        for y in range(self.__rows):
            for x in range(self.__cols):
                self.create_node(x, y)

        for node in self.__graph:
            left_node = Node(node.get_x() - self.__step, node.get_y())
            right_node = Node(node.get_x() + self.__step, node.get_y())
            above_node = Node(node.get_x(), node.get_y() - self.__step)
            below_node = Node(node.get_x(), node.get_y() + self.__step)
            self.__add_connection(node, left_node, 1)
            self.__add_connection(node, right_node, 1)
            self.__add_connection(node, above_node, 1)
            self.__add_connection(node, below_node, 1)

    def remove_node(self, x, y):
        x = x//self.__step
        y = y//self.__step
        node = Node(x, y)
        print(node, "removed")
        left_node = Node(x - self.__step, y)
        right_node = Node(x + self.__step, y)
        above_node = Node(x, y - self.__step)
        below_node = Node(x, y + self.__step)
        self.__remove_connection(node, left_node)
        self.__remove_connection(node, right_node)
        self.__remove_connection(node, above_node)
        self.__remove_connection(node, below_node)
        if node in self.__graph:
            del self.__graph[node]

    def __add_connection(self, node1, node2, weight):
        connection1 = Connection(node2, weight)
        if node1 in self.__graph and node2 in self.__graph:
            self.__graph[node1].append(connection1.get_connection())

    def __remove_connection(self, node1, node2):
        if node2 in self.__graph:
            self.__graph[node2].remove(node1)

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
