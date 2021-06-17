class Walker:
    def __init__(self, graph, start, target):
        self.__graph = graph
        self.__start = start
        self.__target = target

    def get_next_direction(self):
        pass

    def update_graph(self, graph):
        self.__graph = graph
