import pygame
from queue import Queue
from .RP import reconstruct_path

# Traverse the grid and find all nodes connected to the start
def get_unvisited_nodes(start):
    Q = Queue()
    Q_hash = {start}
    Q.put(start)

    while not Q.empty():
        current = Q.get()

        for neighbor in current.neighbors:
            if neighbor not in Q_hash:
                Q.put(neighbor)
                Q_hash.add(neighbor)
    return Q_hash


def bell_ford(draw, start, end, accuracy):
    nodes = get_unvisited_nodes(start)
    
    distance = {node: float("inf") for node in nodes}
    predecessor = {}
    
    distance[start] = 0
    counter = int((len(nodes) - 1) * accuracy)
    run = True
    
    while counter >= 0 and run:
        for current in nodes:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    run = False
            if not current.is_start() and not current.is_end():
                current.uncheck()
            
            draw()
            
            if not current.is_start() and not current.is_end():
                current.check()
            
            for neighbor in current.neighbors:
                if distance[current] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[current] + 1
                    predecessor[neighbor] = current
        counter -= 1
    
    reconstruct_path(predecessor, end, draw)