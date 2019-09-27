import random, turtle, sys

sys.setrecursionlimit(99999999)

def gengrid(sizex, sizey):
    y = []
    for i in range(sizey):
        x = []
        for j in range(sizex):
            x.append('#')
        y.append(x)
    return y

def genmaze(grid, coord):
    possibles = []
    grid[coord[1]][coord[0]] = ' '
    neighbors = getneighbors(coord, 2)
    for i, x in enumerate(neighbors):
        if not (x[0] < 0 or x[1] < 0 or x[0] >= len(grid[0]) or x[1] >= len(grid)) and grid[x[1]][x[0]] == '#':
            possibles.append(x)
    del neighbors[:]

    random.shuffle(possibles)
    for x in possibles:
        while grid[x[1]][x[0]] == '#':
            if coord[0] != x[0]:
                grid[x[1]][(x[0] - coord[0]) // 2 + coord[0]] = ' '
            if coord[1] != x[1]:
                grid[(x[1] - coord[1]) // 2 + coord[1]][x[0]] = ' '
            genmaze(grid, x)
    return grid

def getneighbors(curr, dis):
    neighbors = []
    neighbors.append((curr[0] - dis, curr[1]))
    neighbors.append((curr[0] + dis, curr[1]))
    neighbors.append((curr[0], curr[1] + dis))
    neighbors.append((curr[0], curr[1] - dis))
    return neighbors

def draw(grid, size):
    turtle.ht()
    turtle.speed(0)
    turtle.begin_poly()
    for x in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.end_poly()
    turtle.addshape('block', turtle.get_poly())
    turtle.shape('block')
    turtle.pu()
    turtle.clear()

    furthest = []
    ends = deadends(grid)
    grid[ends[0][1]][ends[0][0]] = 'S'
    for x in ends:
        furthest.append(x[0] + x[1])
    grid[ends[furthest.index(max(furthest))][1]][ends[furthest.index(max(furthest))][0]] = 'E'

    file = "Mazes/maze " + str(len(grid[0]) - 2) + 'x' + str(len(grid) - 2) + ".txt"
    index = open(file, 'w')
    for x in grid:
        index.write(''.join(x) + '\n')
        print(''.join(x))
    index.close()
    
    for n, i in enumerate(grid):
        turtle.setpos(-400, -n*size + 385)
        for j in i:
            if j == '#':
                turtle.pd()
                turtle.stamp()
                turtle.pu()
                turtle.fd(size)
            elif j == 'S':
                turtle.color("Red")
                turtle.pd()
                turtle.stamp()
                turtle.pu()
                turtle.color("Black")
                turtle.fd(size)
            elif j == 'E':
                turtle.pd()
                turtle.color("Green")
                turtle.stamp()
                turtle.color("Black")
                turtle.pu()
                turtle.fd(size)
            else:
                turtle.fd(size)

def deadends(grid):
    ends = []
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            neighbors = getneighbors((x, y), 1)
            count = 0
            if grid[y][x] == ' ':
                for z in neighbors:
                    if grid[z[1]][z[0]] == '#':
                        count += 1
            if count > 2:
                ends.append((x, y))
    return ends

#79 75
print("Dimensions should be odd.")
sizex = int(input("X: ")) + 2
sizey = int(input("Y: ")) + 2
size = int(input("Size: "))
a = genmaze(gengrid(sizex, sizey), (random.randint(0, int(sizex/2) - 1) * 2 + 1, (random.randint(0, int(sizey/2) - 1) * 2 + 1)))
draw(a, size)
turtle.mainloop()
