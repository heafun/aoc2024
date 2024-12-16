file = open("day10/input1.txt")
lines = list(map(lambda x: x.strip(), file.readlines()))
file.close()

def get_trail_head_score(row: int, col: int, destinations: list[tuple[int, int]]):
    score = 0
    current_height = int(lines[row][col])
    
    if current_height == 9 and (row, col) not in destinations:
        destinations.append((row, col))
        return 1
    
    # Up
    if row > 0 and int(lines[row - 1][col]) == current_height + 1:
        score += get_trail_head_score(row - 1, col, destinations)
        
    # Down
    if row < len(lines) - 1 and int(lines[row + 1][col]) == current_height + 1:
        score += get_trail_head_score(row + 1, col, destinations)
        
    # Left
    if col > 0 and int(lines[row][col - 1]) == current_height + 1:
        score += get_trail_head_score(row, col - 1, destinations)
        
    # Right
    if col < len(lines[0]) - 1 and int(lines[row][col + 1]) == current_height + 1:
        score += get_trail_head_score(row, col + 1, destinations)
        
    return score

total_score = 0

for row in range(len(lines)):
    for col in range(len(lines)):
        if lines[row][col] == '0':
            destinations: list[tuple[int, int]] = []
            total_score += get_trail_head_score(row, col, destinations)
            
print(total_score)
