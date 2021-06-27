from Walker import Walker
import heapq as heap
from Snake import Direction



class AStar(Walker):
    def __init__(self,graph,start,target):
        Walker.__init__(self,graph,start,
                        target)


    @staticmethod
    def heauristic(node, goal):
        x1,y1 = node
        x2,y2=goal
        h=abs(x1-x2)+abs(y1-y2)
        return h

    @staticmethod
    def reconstruct_path(cameFrom, current):
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.append(current)
        return total_path

    def get_next_direction(self):

        openSet = []
        cameFrom = {}


        """print('start node',self._start)
        print('end node',self._target)"""

        self._start=(self._start.get_x(),self._start.get_y())
        self._target=(self._target.get_x(),self._target.get_y())

        gscore = {node.get_coordinates(): 9999999 for node in self._graph.get_graph()}
        gscore[self._start] = 0
        fscore = {node.get_coordinates(): 9999999 for node in self._graph.get_graph()}
        fscore[self._start] = self.heauristic(self._start, self._target)

        heap.heappush(openSet, [fscore[self._start], self._start])

        while openSet:

            current=heap.heappop(openSet)  # O(1)
            # print(current)

            if current[1] == self._target:
                path = self.reconstruct_path(cameFrom, current[1])
                path = path[::-1]
                if len(path) == 1:
                    nextmove = path[0]

                else:
                    nextmove = path[1]

                """print("path equal ", path)
                print('nextmove', nextmove)"""
                # print('start',self._start)
                if nextmove[0] > self._start[0]:
                    return Direction.RIGHT
                elif nextmove[0] < self._start[0]:
                    return Direction.LEFT
                elif nextmove[1] > self._start[1]:
                    return Direction.DOWN
                elif nextmove[1] < self._start[1]:
                    return Direction.UP
                else:
                    #print('first false')
                    return False

            for neighbour in self._graph.get_node_connections(current[1][0], current[1][1]):

                neighbour = neighbour.get_connection()
                neighbourNode = neighbour[0]

                #print(neighbourNode)
                neighbourWeight = neighbour[1]
                tentative_gscore = gscore[current[1]]+neighbourWeight

                if tentative_gscore<gscore[neighbourNode]:
                    cameFrom[neighbourNode] = current[1]

                    gscore[neighbourNode] = tentative_gscore
                    fscore[neighbourNode] = gscore[neighbourNode]+self.heauristic(neighbourNode, self._target)
                    if neighbourNode not in openSet:
                        heap.heappush(openSet, [fscore[neighbourNode], neighbourNode])


        print('no path ')


        """if currdir == Direction.RIGHT:
            return Direction.LEFT
        elif currdir == Direction.LEFT:
            return Direction.RIGHT
        elif currdir == Direction.UP:
            return Direction.DOWN
        elif currdir == Direction.DOWN:
            return Direction.UP"""

        return Direction.NONE
