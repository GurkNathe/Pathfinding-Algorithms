import pygame
from .RP import reconstruct_path

"""
Recursive
1. Mark the current node as visited(initially current node is the root node)
2. Check if current node is the goal, If so, then return it.
3. Iterate over children nodes of current node, and do the following:
    1. Check if a child node is not visited.
    2. If so, then, mark it as visited.
    3. Go to it's sub tree recursively until you find the goal node(In other words, do the same steps here passing the child node as the current node in the next recursive call).
    4. If the child node has the goal node in this sub tree, then, return it.
3. If goal node is not found, then goal node is not in the tree!


Iterative
1. Add root node to the stack.
2. Loop on the stack as long as it's not empty.
    1. Get the node at the top of the stack(current), mark it as visited, and remove it.
    2. For every non-visited child of the current node, do the following:
        1. Check if it's the goal node, If so, then return this child node.
        2. Otherwise, push it to the stack.
3. If stack is empty, then goal node was not found!
"""


def dfs(draw, start, end):
    stack = [start]
    previous = {}

    found = False
    run = True

    while len(stack) and not found and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False

        current = stack.pop()

        if current.is_checked():
            continue

        # Drawing stuff
        if current != start:
            current.uncheck()

        draw()

        if current != start:
            current.check()

        # Find unvisited neighbors and check for end
        for neighbor in current.neighbors:
            if not neighbor.is_checked():
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    break
                else:
                    previous[neighbor] = current
                    stack.append(neighbor)

    reconstruct_path(previous, end, draw)
