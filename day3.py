with open('aoc2019_3.txt', 'r') as f:
    data = f.readlines()
data = [line.rstrip('\n') for line in data]

wire_a_vectors = data[0].split(',')
wire_b_vectors = data[1].split(',')

def move(x,y,vector):
    direction = vector[0]
    magnitude = int(vector[1:])
    if direction in 'LR':
        if direction == 'L':
            points = [(x-m,y) for m in range(1,magnitude+1)]
        else:
            points = [(x+m,y) for m in range(1,magnitude+1)]
    else:
        if direction == 'D':
            points = [(x,y-m) for m in range(1,magnitude+1)]
        else:
            points = [(x,y+m) for m in range(1,magnitude+1)]
    return points

def manhattan(point):
    x,y = point
    return abs(x)+abs(y)

x,y = 0,0
wire_a_points = []
for v in wire_a_vectors:
    points = move(x,y,v)
    x,y = points[-1]
    wire_a_points += points
    
x,y = 0,0
wire_b_points = []
for v in wire_b_vectors:
    points = move(x,y,v)
    x,y = points[-1]
    wire_b_points += points
    
    
crossings = list(set(wire_b_points ).intersection(set(wire_a_points)))

part1 = min(manhattan(point) for point in crossings)

part2 = min(wire_a_points.index(c)+wire_b_points.index(c)+2 for c in crossings)

print(f'part1= {part1}   part2= {part2}')
