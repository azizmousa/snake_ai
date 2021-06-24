class Walker:
    def __init__(self, graph, start, target):
        self._graph = graph
        self._start = start
        self._target = target
        self._graph_updated = True

    def get_next_direction(self):
        pass

    def update_graph(self, graph, start, target):
        self._graph = graph
        self._start = start
        self._target = target
        self._graph_updated = True

    def is_graph_updated(self):
        ret = self._graph_updated
        self._graph_updated = False
        return ret
