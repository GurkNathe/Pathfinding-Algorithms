import random

# Based on the code from here:
# https://github.com/OrWestSide/python-scripts/blob/master/maze.py

def surroundingCells(grid, y, x):
    s_cells = 0
    if grid[y - 1][x].is_unchecked():
        s_cells += 1
    if grid[y + 1][x].is_unchecked():
        s_cells += 1
    if grid[y][x - 1].is_unchecked():
        s_cells +=1
    if grid[y][x + 1].is_unchecked():
        s_cells += 1    
    
    return s_cells

def delete_wall(walls, rand_wall):
    r_x, r_y = rand_wall.get_pos()
    for wall in walls:
        w_x, w_y = wall.get_pos()
        if w_x == r_x and w_y == r_y:
            walls.remove(wall) 

def check_up(grid, walls, r_y, r_x):
    if r_y != 0:
        if not grid[r_y - 1][r_x].is_unchecked():
            grid[r_y - 1][r_x].make_obstacle()
        if grid[r_y - 1][r_x] not in walls:
            walls.append(grid[r_y - 1][r_x])

def check_down(grid, walls, r_y, r_x, height):
    if r_y != height - 1:
        if not grid[r_y + 1][r_x].is_unchecked():
            grid[r_y + 1][r_x].make_obstacle()
        if grid[r_y + 1][r_x] not in walls:
            walls.append(grid[r_y + 1][r_x])

def check_left(grid, walls, r_y, r_x):
    if r_x != 0:
        if not grid[r_y][r_x - 1].is_unchecked():
            grid[r_y][r_x - 1].make_obstacle()
        if grid[r_y][r_x - 1] not in walls:
            walls.append(grid[r_y][r_x - 1])

def check_right(grid, walls, r_y, r_x, width):
    if r_x != width - 1:
        if grid[r_y][r_x + 1].is_unchecked():
            grid[r_y][r_x + 1].make_obstacle()
        if grid[r_y][r_x + 1] not in walls:
            walls.append(grid[r_y][r_x + 1])

def gen_maze(grid, start, end):
    height = len(grid)
    width = len(grid[0])
    
    start_height = random.randint(1, len(grid) - 2)
    start_width = random.randint(1, len(grid[0]) - 2)
    
    walls = []
    
    grid[start_height][start_width].uncheck()
    
    walls.append(grid[start_height - 1][start_width])
    walls.append(grid[start_height][start_width - 1])
    walls.append(grid[start_height][start_width + 1])
    walls.append(grid[start_height + 1][start_width])
    
    for node in walls:
        node.make_obstacle()

    while walls:
        
        rand_wall = walls[int(random.random() * len(walls)) - 1]
        
        r_y, r_x = rand_wall.get_pos()
        
        if r_x != 0:
            if grid[r_y][r_x - 1].is_default() and grid[r_y][r_x + 1].is_unchecked():
                s_cells = surroundingCells(grid, r_y, r_x)
                if s_cells < 2:
                    grid[r_y][r_x].uncheck()
                    
                    check_up(grid, walls, r_y, r_x)
                    check_down(grid, walls, r_y, r_x, height)
                    check_left(grid, walls, r_y, r_x)

                delete_wall(walls, rand_wall)
                continue
        
        if r_y != 0:
            if grid[r_y - 1][r_x].is_default() and grid[r_y + 1][r_x].is_unchecked():
                s_cells = surroundingCells(grid, r_y, r_x)
                if s_cells < 2:
                    grid[r_y][r_x].uncheck()
                    
                    check_up(grid, walls, r_y, r_x)
                    check_left(grid, walls, r_y, r_x)
                    check_right(grid, walls, r_y, r_x, width)
                    
                delete_wall(walls, rand_wall)
                continue
        
        if r_y != height - 1:
            if grid[r_y + 1][r_x].is_default() and grid[r_y - 1][r_x].is_unchecked():
                s_cells = surroundingCells(grid, r_y, r_x)
                if s_cells < 2:
                    grid[r_y][r_x].uncheck()
                    
                    check_down(grid, walls, r_y, r_x, height)
                    check_left(grid, walls, r_y, r_x)
                    check_right(grid, walls, r_y, r_x, width)
                            
                delete_wall(walls, rand_wall)
                continue
        
        if r_x != width - 1:
            if grid[r_y][r_x + 1].is_default() and grid[r_y][r_x - 1].is_unchecked():
                s_cells = surroundingCells(grid, r_y, r_x)
                if s_cells < 2:
                    grid[r_y][r_x].uncheck()
                    
                    check_right(grid, walls, r_y, r_x, width)
                    check_down(grid, walls, r_y, r_x, height)
                    check_up(grid, walls, r_y, r_x)
                    
                delete_wall(walls, rand_wall)
                continue
        
        delete_wall(walls, rand_wall)
    
    # Make remaining unvisited cells walls
    for row in grid:
        for node in row:
            if node.is_default():
                node.make_obstacle()
    
    # Set start and end
    while not start:
        node = random.randint(1, width - 1)
        
        if grid[1][node].is_unchecked():
            start = grid[0][node]
            start.make_start()
            break
    
    while not end:
        node = random.randint(1, width - 1)
        
        if grid[height - 2][node].is_unchecked():
            end = grid[height - 1][node]
            end.make_end()
            break
    
    # Clear unchecks
    for row in grid:
        for node in row:
            if node.is_unchecked():
                node.reset()
    
    return start, end