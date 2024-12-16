from typing import List


file = open("day4/input1.txt")
lines: List[str] = file.readlines()
file.close()

# Remove new line chars
lines = list(map(lambda x: x.strip(), lines))

search_strings: List[str] = list()

# Horizontal
search_strings.extend(lines)

#Vertical
for column in range(len(lines[0])):
    column_string = ''
    
    for row in range(len(lines)):
        column_string += lines[row][column]
        
    search_strings.append(column_string)
    
# Fill lines above to make iterating diagonals easier
fill_line = '#' * len(lines[0])

for i in range(len(lines[0])):
    lines.insert(0, fill_line)
    
    
#Diagonals
for row in range(len(lines)):
    diagonal_string1 = ''
    diagonal_string2 = ''
    
    for i in range(min(len(lines[0]), len(lines) - row)):
        diagonal_string1 += lines[row + i][i]
        diagonal_string2 += lines[row + i][abs(i - len(lines[0])) - 1]
        
    search_strings.append(diagonal_string1)
    search_strings.append(diagonal_string2)
    
xmas = 'XMAS'
xmas_rev = xmas[::-1]

xmas_count = 0

for search_string in search_strings:
    if search_string == xmas or search_string == xmas_rev:
        xmas_count += 1
        continue
    
    xmas_count += len(search_string.split(xmas)) - 1
    xmas_count += len(search_string.split(xmas_rev)) - 1
    
print(xmas_count)
