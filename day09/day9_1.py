file = open("day9/input1.txt")
line = list(map(lambda x: int(x), file.readline().strip()))
file.close()

file_blocks: list[int] = []

file_id = 0

for i in range(0, len(line), 2):
    file_blocks.extend([file_id for _ in range(line[i])])
    
    if i + 1 < len(line):
        file_blocks.extend([-1 for _ in range(line[i + 1])])
        
    file_id += 1

index = 0

while True:
    if index >= len(file_blocks):
        break
    
    if file_blocks[index] == -1:
        file_blocks[index] = file_blocks[-1]
        del file_blocks[-1]
    
    for i in range(len(file_blocks) - 1, -1, -1):
        if file_blocks[i] == -1:
            del file_blocks[i]
        else:
            break
    
    index += 1
    
checksum = 0

for position, block_id in enumerate(file_blocks):
    checksum += position * block_id

print(checksum)
