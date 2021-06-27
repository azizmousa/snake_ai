from Game import Game
from BFS import Bfs
from Dijikstra import Dijikstra
from Astar import AStar
if __name__ == '__main__':
    bfs = Bfs(None, None, None)
    a_star = AStar(None, None, None)
    dij = Dijikstra(None, None, None)
    game = Game(bfs, 1000, 500)
    game.start()
