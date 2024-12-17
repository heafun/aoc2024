file = open("day11/input1.txt")
stones = list(map(lambda x: int(x), file.readline().split()))
file.close()

def add_to_dict(key: int, value: int, dict: dict):
    if key in dict.keys():
        dict[key] += value
    else:
        dict[key] = value

stone_memory: dict[int, tuple[int, int]] = dict()
total_stones = 0

for stone in stones:
    stone_dict: dict[int, int] = { stone:1 }
    
    for _ in range(75):
        new_stone_dict = dict()
        
        for key in stone_dict.keys():
            if key == -1:
                continue
            
            if key in stone_memory:
                add_to_dict(stone_memory[key][0], stone_dict[key], new_stone_dict)
                add_to_dict(stone_memory[key][1], stone_dict[key], new_stone_dict)
            else:
                if key == 0:
                    stone_memory[key] = (1, -1)                    
                    add_to_dict(stone_memory[key][0], stone_dict[key], new_stone_dict)
                elif len(str(key)) % 2 == 0:
                    stone_str = str(key)
                    
                    stone_memory[key] = (int(stone_str[:int(len(stone_str)/2)]), int(stone_str[int(len(stone_str)/2):]))
                    add_to_dict(stone_memory[key][0], stone_dict[key], new_stone_dict)
                    add_to_dict(stone_memory[key][1], stone_dict[key], new_stone_dict)
                else:
                    stone_memory[key] = (key * 2024, -1)
                    add_to_dict(stone_memory[key][0], stone_dict[key], new_stone_dict)
        
        stone_dict = new_stone_dict
    
    stone_dict.pop(-1, None)   
    total_stones += sum(stone_dict.values())

print(total_stones)
