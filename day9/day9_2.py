import copy
from functools import reduce
import operator


file = open("day9/input1.txt")
disk_map = list(map(lambda x: int(x), file.readline().strip()))
file.close()

file_list: list[int] = []
space_list: list[int] = []

for i in range(0, len(disk_map), 2):
    file_list.append(disk_map[i])
    
    if i + 1 < len(disk_map):
        space_list.append(disk_map[i + 1])
        
space_list.append(0)
file_index_dict: dict[int] = dict(enumerate(range(len(file_list))))

for file_id in range(len(file_list)-1, -1, -1):
    # print(str(file_id) + '/' + str(len(file_list)))
    for space_index in range(len(space_list)):
        file_index = file_index_dict[file_id]
        
        if space_index >= file_index:
            break
        
        if file_list[file_id] <= space_list[space_index]:
            space_list[file_index - 1] += space_list[file_index] + file_list[file_id]
            space_list.pop(file_index)
            
            old_index = file_index_dict[file_id]
            file_index_dict[file_id] = space_index + 1
            for id, i in enumerate(file_index_dict):                            
                if id != file_id and file_index_dict[i] >= space_index + 1 and file_index_dict[i] < old_index:
                    file_index_dict[i] += 1
            
            space_list[space_index] -= file_list[file_id]
            space_list.insert(space_index, 0)
            break

compressed_file_list = [0 for _ in range(len(file_index_dict))]

for id in range(len(file_index_dict)):
    compressed_file_list[file_index_dict[id]] = id
        
disk_map: list[int] = reduce(operator.add, zip(compressed_file_list, space_list))

position = 0
checksum = 0

for index in range(0, len(disk_map), 2):
    for _ in range(file_list[disk_map[index]]):
        checksum += position * disk_map[index]
        position += 1
        
    position += disk_map[index + 1]
    
print(checksum)
