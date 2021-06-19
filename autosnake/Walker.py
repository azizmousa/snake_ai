class Walker:
    def __init__(self, graph, start, target):
        self._graph = graph
        self._start = start
        self._target = target

    def get_next_direction(self):
        pass

    def update_graph(self, graph):
        self._graph = graph
