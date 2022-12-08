import pygame
import math
from queue import PriorityQueue
from .RP import reconstruct_path

"""
function theta*(start, goal)
    // This main loop is the same as A*
    gScore(start) := 0
    parent(start) := start
    // Initializing open and closed sets. The open set is initialized 
    // with the start node and an initial cost
    open := {}
    open.insert(start, gScore(start) + heuristic(start))
    // gScore(node) is the current shortest distance from the start node to node
    // heuristic(node) is the estimated distance of node from the goal node
    // there are many options for the heuristic such as Euclidean or Manhattan 
    closed := {}
    while open is not empty
        s := open.pop()
        if s = goal
            return reconstruct_path(s)
        closed.push(s)
        for each neighbor of s
        // Loop through each immediate neighbor of s
            if neighbor not in closed
                if neighbor not in open
                    // Initialize values for neighbor if it is 
                    // not already in the open list
                    gScore(neighbor) := infinity
                    parent(neighbor) := Null
                update_vertex(s, neighbor)
    return Null
            
    
function update_vertex(s, neighbor)
    // This part of the algorithm is the main difference between A* and Theta*
    if line_of_sight(parent(s), neighbor)
        // If there is line-of-sight between parent(s) and neighbor
        // then ignore s and use the path from parent(s) to neighbor 
        if gScore(parent(s)) + c(parent(s), neighbor) < gScore(neighbor)
            // c(s, neighbor) is the Euclidean distance from s to neighbor
            gScore(neighbor) := gScore(parent(s)) + c(parent(s), neighbor)
            parent(neighbor) := parent(s)
            if neighbor in open
                open.remove(neighbor)
            open.insert(neighbor, gScore(neighbor) + heuristic(neighbor))
    else
        // If the length of the path from start to s and from s to 
        // neighbor is shorter than the shortest currently known distance
        // from start to neighbor, then update node with the new distance
        if gScore(s) + c(s, neighbor) < gScore(neighbor)
            gScore(neighbor) := gScore(s) + c(s, neighbor)
            parent(neighbor) := s
            if neighbor in open
                open.remove(neighbor)
            open.insert(neighbor, gScore(neighbor) + heuristic(neighbor))

function reconstruct_path(s)
    total_path = {s}
    // This will recursively reconstruct the path from the goal node 
    // until the start node is reached
    if parent(s) != s
        total_path.push(reconstruct_path(parent(s)))
    else
        return total_path
"""


def euclidean(node1, node2):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Returns true if there is a direct line of sight between two nodes
def line_of_sight(node1, node2):
    # Check if node1 is from the same index as node2
    # If so, return true
    pass


def remove_add(open_set_hash, open_set, distance, counter, neighbor):
    if neighbor in open_set_hash:
        open_set_hash.remove(neighbor)
        open_set.queue.remove(neighbor)
    open_set.put(
        (
            distance,
            counter,
            neighbor,
        )
    )
    open_set_hash[neighbor] = distance


def update_vertex(
    current, neighbor, parent, g_score, open_set, open_set_hash, end, counter
):
    h = heuristic(neighbor.get_pos(), end.get_pos())
    if line_of_sight(parent[current], neighbor):
        g_p_curr = g_score[parent[current]] + euclidean(parent[current], neighbor)
        if g_p_curr < g_score[neighbor]:
            g_score[neighbor] = g_p_curr
            parent[neighbor] = parent[current]
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )
    else:
        g_curr = g_score[current] + euclidean(current, neighbor)
        if g_curr < g_score[neighbor]:
            g_score[neighbor] = g_curr
            parent[neighbor] = current
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )


# Manhattan distance
def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def theta_star(draw, start, end):
    g_score = {}
    g_score[start] = 0

    previous = {}

    counter = 0
    open_set = PriorityQueue()
    open_set.put(
        (g_score[start] + heuristic(start.get_pos(), end.get_pos()), counter, start)
    )
    open_set_hash = {start}

    parent = {}
    parent[start] = start

    while open_set:
        current = open_set.get()

        if current.is_end():
            reconstruct_path(previous, end, draw)
            break

        if not current.is_start():
            current.check()
        else:
            current.been_checked = True

        for neighbor in current.neighbors:
            if not neighbor.been_checked:
                if not neighbor in open_set_hash:
                    g_score[neighbor] = float("inf")
                    parent[neighbor] = None

                update_vertex(
                    current,
                    neighbor,
                    parent,
                    g_score,
                    open_set,
                    open_set_hash,
                    end,
                    counter,
                )
