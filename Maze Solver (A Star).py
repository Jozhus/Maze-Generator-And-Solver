import queue
import turtle

def heur(curr):
    return abs(abs(curr[0]) - abs(end[0])) + abs(abs(curr[1]) - abs(end[1]))

        
def getneighbors(curr):
    neighbors = []
    directions = [(curr[0], curr[1] - 1), (curr[0], curr[1] + 1), (curr[0] - 1, curr[1]), (curr[0] + 1, curr[1])]
    for x in directions:
        if importedmaze[x[1]][x[0]] == ' ':
            neighbors.append((x))
    return neighbors

importedmaze = [list(line.rstrip('\n')) for line in open("G:/Users/Jozhus/Documents/Python/Mazes/" + str(input("Maze name: ")) + ".txt")]

for y in importedmaze:
    if 'S' in y:
        start = (y.index('S'), importedmaze.index(y))
    if 'E' in y:
        end = (y.index('E'), importedmaze.index(y))

openlist = queue.PriorityQueue()
openlist.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not openlist.empty():
    current = openlist.get()

    if current == end:
        break
   
    for next in getneighbors(current):
        new_cost = cost_so_far[current] + 1
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost + heur(next)
            openlist.put(next, priority)
            came_from[next] = current

for x in getneighbors(end):
    if x in came_from:
        path = [x]
for x in range(len(came_from) - 1):
    if came_from[path[-1]] == None:
        path.append(end)
        break
    path.append(came_from[path[-1]])
path = list(reversed(path))

for x in path:
    if importedmaze[x[1]][x[0]] != 'S' and importedmaze[x[1]][x[0]] != 'E':
        importedmaze[x[1]][x[0]] = 'X'

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

    file = "G:/Users/Jozhus/Documents/Python/Mazes/maze " + str(len(grid[0]) - 2) + 'x' + str(len(grid) - 2) + " Solution" + ".txt"
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
            elif j == 'X':
                turtle.pd()
                turtle.color("Blue")
                turtle.stamp()
                turtle.color("Black")
                turtle.pu()
                turtle.fd(size)
            else:
                turtle.fd(size)

draw(importedmaze, int(input("Size: ")))
turtle.mainloop()
