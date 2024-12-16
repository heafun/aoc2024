file = open("day1/input1.txt")
lines = file.readlines()
file.close()

left_list = []
right_dict = dict()

for line in lines:
    line_parts = line.split()
    left_list.append(int(line_parts[0]))
    right_id = int(line_parts[1])
    
    if right_id in right_dict.keys():
        right_dict[right_id] += 1
    else:
        right_dict[right_id] = 1

sum = 0

for id in left_list:
    sum += id * right_dict.get(id, 0)
    
print(sum)
