import pygame
from queue import PriorityQueue
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

# Manhattan distance
def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def gbfs(draw, start, end):
    Q = PriorityQueue()
    Q.put((heuristic(start.get_pos(), end.get_pos()), 0, start))
    
    counter = 0
    run = True
    found = False
    
    previous = { }
    
    while not Q.empty() and run and not found:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False
        
        current = Q.get()
        
        if current[2].is_checked():
            continue
        
        if not current[2].is_start() and not current[2].is_end():
            current[2].uncheck()

        draw()
        
        if not current[2].is_start() and not current[2].is_end():
            current[2].check()
        
        largest = (None, None, None)
        for neighbor in current[2].neighbors:
            if not neighbor.is_checked():
                if neighbor.is_end():
                    previous[neighbor] = current[2]
                    found = True
                    break
                
                counter += 1
                distance = heuristic(neighbor.get_pos(), end.get_pos())
                largest = (distance, counter, neighbor)
                previous[largest[2]] = current[2]
                Q.put(largest)
        
    reconstruct_path(previous, end, draw)