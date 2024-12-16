file = open("day10/input1.txt")
lines = list(map(lambda x: x.strip(), file.readlines()))
file.close()

def get_trail_head_score(row: int, col: int):
    score = 0
    current_height = int(lines[row][col])
    
    if current_height == 9:
        return 1
    
    # Up
    if row > 0 and int(lines[row - 1][col]) == current_height + 1:
        score += get_trail_head_score(row - 1, col)
        
    # Down
    if row < len(lines) - 1 and int(lines[row + 1][col]) == current_height + 1:
        score += get_trail_head_score(row + 1, col)
        
    # Left
    if col > 0 and int(lines[row][col - 1]) == current_height + 1:
        score += get_trail_head_score(row, col - 1)
        
    # Right
    if col < len(lines[0]) - 1 and int(lines[row][col + 1]) == current_height + 1:
        score += get_trail_head_score(row, col + 1)
        
    return score

total_score = 0

for row in range(len(lines)):
    for col in range(len(lines)):
        if lines[row][col] == '0':
            total_score += get_trail_head_score(row, col)
            
print(total_score)
