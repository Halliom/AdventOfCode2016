data = map(lambda x: x.strip(), open("input.txt").read().split(','))
# Start at the origin (0, 0)
p = (0, 0)
# Start facing upwards (positive y)
facing = (0, 1)
visited = []

def run():
    global data, p, facing, visited
    for i in data:
        if i[0] == 'R':
            newFacing = (facing[1], -facing[0])
        else:
            newFacing = (-facing[1], facing[0])
        for j in range(int(i[1:])):
            p = (p[0] + newFacing[0], p[1] + newFacing[1])
            if p in visited:
                return
            visited.append(p)
        facing = newFacing
run()
print(abs(p[0]) + abs(p[1]))
