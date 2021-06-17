class Connection:
    def __init__(self, node, weight):
        self.__node = node
        self.__weight = weight

    def get_node(self):
        return self.__node

    def get_weight(self):
        return self.__weight

    def get_connection(self):
        return self.__node, self.__weight
