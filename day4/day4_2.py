from typing import List


file = open("day4/input1.txt")
lines: List[str] = file.readlines()
file.close()

# Remove new line chars
lines = list(map(lambda x: x.strip(), lines))

def is_valid_x(row: int, col: int):
    mas = 'MAS'
    mas_rev = mas[::-1]
    
    #   -1 c +1
    #-1 #  .  #
    # r .  #  .
    #+1 #  .  #
    
    diagonal1 = lines[row-1][col-1] + lines[row][col] + lines[row+1][col+1]
    diagonal2 = lines[row+1][col-1] + lines[row][col] + lines[row-1][col+1]
    
    if (diagonal1 == mas or diagonal1 == mas_rev) and (diagonal2 == mas or diagonal2 == mas_rev):
        return True
    
    return False

x_count = 0

for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[0]) - 1):
        x_count += 1 if is_valid_x(row, col) else 0
        
print(x_count)
