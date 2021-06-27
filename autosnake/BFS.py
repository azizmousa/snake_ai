from Walker import Walker
from Node import Node
from Snake import Direction


class Bfs(Walker):
    def __init__(self, graph, start, target):
        super().__init__(graph, start, target)
        self._current_node = start
        self._direction_list = []
        self._current_direction = Direction.NONE

    def get_next_direction(self):
        path = self.bfs(self._graph.get_graph(), self._start, self._target)
        # print("path>>>>>>>>>>>>>>>>", path)
        if len(path) > 0:
            new_node = path.pop(0)
            # print("go from:", self._current_node, "to:", new_node)
            dr = self._get_direction(self._current_node, new_node)
            self._current_node = new_node
            self._current_direction = dr
            return dr
        else:
            # if self._current_direction == Direction.LEFT:
            #     return Direction.RIGHT
            # elif self._current_direction == Direction.RIGHT:
            #     return Direction.LEFT
            # elif self._current_direction == Direction.UP:
            #     return Direction.DOWN
            # elif self._current_direction == Direction.DOWN:
            return Direction.NONE

    @staticmethod
    def _get_direction(current, new_node):
        if current.get_x() > new_node.get_x():
            return Direction.LEFT
        elif current.get_x() < new_node.get_x():
            return Direction.RIGHT
        elif current.get_y() > new_node.get_y():
            return Direction.UP
        elif current.get_y() < new_node.get_y():
            return Direction.DOWN
        else:
            return Direction.NONE

    def update_graph(self, graph, start, target):
        super().update_graph(graph, start, target)
        self._current_node = start
        self._direction_list = []

    def bfs(self, graph_list, start, target):
        # print("start:", start)
        # print("target:", target)
        queue = Queue()
        itr = iter(graph_list)
        visited = dict(zip(itr, [False] * len(graph_list)))
        path = []
        itr = iter(graph_list)
        prev = dict(zip(itr, [Node(-1, -1)] * self._graph.get_graph_size()))
        queue.add(start)

        while False in visited.values():
            if queue.size() == 0:
                return path
            node = queue.remove()
            if node in visited and not visited[node]:
                if not node == start:
                    self._direction_list.append(node)

                for n in graph_list[node]:
                    if not visited[n.get_node()]:
                        visited[node] = True
                        prev[n.get_node()] = node
                        queue.add(n.get_node())

                    if node == target:
                        d = target
                        while d in prev:
                            path.append(d)
                            d = prev[d]

                        path.reverse()
                        path.pop(0)
                        return path


class Queue:
    def __init__(self):
        self.data = []

    def add(self, element):
        self.data.append(element)

    def remove(self):
        if len(self.data) == 0:
            raise Exception("Queue is empty you cannot remove any element.")
        element = self.get_front()
        del self.data[0]
        return element

    def is_empty(self):
        return len(self.data) == 0

    def get_front(self):
        if self.is_empty():
            raise Exception("Queue is empty you cannot get any element.")
        return self.data[0]

    def get_end(self):
        if self.is_empty():
            raise Exception("Queue is empty you cannot get any element.")
        return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)
