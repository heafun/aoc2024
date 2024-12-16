import copy
from enum import Enum


file = open("day6/input1.txt")
lines = list(map(lambda x: x.strip(), file.readlines()))
file.close()

lines = list(map(lambda x: list(x), lines))

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
class Point:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.is_end = False

def walk(start: Point, direction: Direction) -> Point:
    destination = copy.copy(start)
    
    step_row = 0
    step_col = 0
    
    if direction == Direction.DOWN or direction == Direction.UP:
        step_row = 1 if direction == Direction.DOWN else -1
    
    if direction == Direction.RIGHT or direction == Direction.LEFT:
        step_col = 1 if direction == Direction.RIGHT else -1
    
    stop_row = len(lines) - 1 if direction == Direction.DOWN else 0
    stop_col = len(lines[0]) - 1 if direction == Direction.RIGHT else 0
    
    prevdestination = copy.copy(destination)
    
    while True:
        if lines[destination.row][destination.col] == '#':
            return prevdestination
        
        lines[destination.row][destination.col] = 'X'
        
        if destination.row == stop_row or destination.col == stop_col:
            destination.is_end = True                      
            return destination
        
        prevdestination = copy.copy(destination)
        
        destination.row += step_row
        destination.col += step_col
        
def get_next_direction(direction: Direction) -> Direction:
    match direction:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP      
  
start: Point
direction = Direction.UP
  
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == '^':
            start = Point(row, col)
        
while True:
    start = walk(start, direction)
    
    if start.is_end:
        break
    
    direction = get_next_direction(direction)
    
visited_positions = 0

for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == 'X':
            visited_positions += 1
            
print(visited_positions)
