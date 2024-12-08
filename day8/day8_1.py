file = open("day8/input1.txt")
lines = list(map(lambda x: x.strip(), file.readlines()))
file.close()

antinodes: list[list[bool]] = []
antenna_types: list = []

for row in range(len(lines)):
    antinodes.append([])    
    for col in range(len(lines)):
        antinodes[row].append(False)
        
        if lines[row][col] != '.' and lines[row][col] not in antenna_types:
            antenna_types.append(lines[row][col])
            
def add_antinodes_for_antennas(antenna1: tuple[int, int], antenna2: tuple[int, int]):
    offset = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])
    
    row1 = antenna1[0] + offset[0]
    col1 = antenna1[1] + offset[1]
    
    row2 = antenna2[0] - offset[0]
    col2 = antenna2[1] - offset[1]
    
    if 0 <= row1 and row1 < len(lines) and 0 <= col1 and col1 < len(lines[0]):
        antinodes[row1][col1] = True
    
    if 0 <= row2 and row2 < len(lines) and 0 <= col2 and col2 < len(lines[0]):
        antinodes[row2][col2] = True
    
def find_all_antinodes_for_antenna(antenna: tuple[int, int]):
    index = antenna[0] * len(lines[0]) + antenna[1] + 1
    stop = len(lines) * len(lines[0])
    antenna_type = lines[antenna[0]][antenna[1]]
    
    while index < stop:
        row = int(index / len(lines[0]))
        col = index % len(lines[0])
        
        if lines[row][col] == antenna_type:
            add_antinodes_for_antennas(antenna, (row, col))
            
        index += 1

for antenna_type in antenna_types:
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == antenna_type:
                find_all_antinodes_for_antenna((row, col))

print(sum([sum(line) for line in antinodes]))
