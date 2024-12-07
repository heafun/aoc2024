import copy
from enum import Enum


file = open("day6/input1.txt")
lines = list(map(lambda x: x.strip(), file.readlines()))
file.close()

lines = list(map(lambda x: list(x), lines))
original_lines = copy.deepcopy(lines)

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

def walk(scenario: list[list[str]], start: Point, direction: Direction) -> Point:
    destination = copy.copy(start)
    
    step_row = 0
    step_col = 0
    
    if direction == Direction.DOWN or direction == Direction.UP:
        step_row = 1 if direction == Direction.DOWN else -1
    
    if direction == Direction.RIGHT or direction == Direction.LEFT:
        step_col = 1 if direction == Direction.RIGHT else -1
    
    stop_row = len(scenario) - 1 if direction == Direction.DOWN else 0
    stop_col = len(scenario[0]) - 1 if direction == Direction.RIGHT else 0
    
    prevdestination = copy.copy(destination)
    
    while True:
        if scenario[destination.row][destination.col] == '#':
            return prevdestination
        
        scenario[destination.row][destination.col] = 'X'
        
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
        
original_start = copy.copy(start)
        
while True:
    start = walk(lines, start, direction)
    
    if start.is_end:
        break
    
    direction = get_next_direction(direction)
    
scenarios: list[list[list[str]]] = []

for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == 'X' and not (row == original_start.row and col == original_start.col):
            scenario = copy.deepcopy(original_lines)
            scenario[row][col] = '#'
            scenarios.append(scenario)
            
valid_points = 0

for scenario in scenarios:
    scenario_start = copy.copy(original_start)
    scenario_direction = Direction.UP
    turning_points: list[tuple] = [(copy.copy(scenario_start), scenario_direction)]
    
    while True:
        scenario_start = walk(scenario, scenario_start, scenario_direction)
        scenario_direction = get_next_direction(scenario_direction)
        
        if scenario_start.is_end:
            break
        
        if any(x for x in turning_points if x[0].row == scenario_start.row and x[0].col == scenario_start.col and x[1] == scenario_direction):
            valid_points += 1
            break
        else:
            turning_points.append((copy.copy(scenario_start), scenario_direction))
        
print(valid_points)
