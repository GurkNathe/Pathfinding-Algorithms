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

def b_first_s(draw, start, end):
    Q = PriorityQueue()
    Q.put((0, start))
    
    while not Q.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False
        
        current = Q.get()
        
        if current[1].is_end():
            break
        else:
            for neighbor in current[1].neighbors:
                if not neighbor.is_checked():
                    Q.put((current[0] + 1, neighbor))
            
            if not current[1].is_start() and not current[1].is_end():
                current[1].uncheck()
            
            draw()
            
            if not current[1].is_start() and not current[1].is_end():
                current[1].check()
    pass