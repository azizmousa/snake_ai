import heapq as heap
from Walker import Walker
from Snake import Direction

class Dijikstra(Walker):
    def __init__(self,graph,start,target):
        Walker.__init__(self,graph,start,target)      
        
        
    def get_next_direction(self):
        path = []
        pq = []
        start=(self._start.get_x(),self._start.get_y())
        target=(self._target.get_x(),self._target.get_y())
        distances = {nodes.get_coordinates(): float('inf') for nodes in self._graph.get_graph()}
        distances[start] = 0

        prev = {nodes.get_coordinates(): None for nodes in self._graph.get_graph()} 

        heap.heappush(pq, [distances[start], start])
        path = [target]
       
        while len(pq):

            distance,vertex=heap.heappop(pq)
            for node in self._graph.get_node_connections(vertex[0],vertex[1]):
                node = node.get_connection()
                nodeTuple = node[0]
                nodeWeight = node[1]
                current_dist=distances[vertex]+nodeWeight
                if current_dist<distances[nodeTuple]:
                    distances[nodeTuple]=current_dist
                    prev[nodeTuple]=(vertex[0],vertex[1])
                    heap.heappush(pq, [distances[nodeTuple],nodeTuple])
                    
        current_node=target

        while prev[current_node] is not None:

            
            path.append(prev[current_node])
            current_node=prev[current_node]

        path = path[::-1]
        if len(path)==1:
            path=path[0]
            print('inside if')
        else:
            print('inside else',path)
            
            path=path[1]
            print(path)
        if path[0] > self._start.get_x():
            return Direction.RIGHT
        elif path[0] < self._start.get_x():
            return Direction.LEFT 
        elif path[1] > self._start.get_y():
            return Direction.DOWN 
        elif path[1] < self._start.get_y():
            return Direction.UP
        else:
            False
