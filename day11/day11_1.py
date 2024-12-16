file = open("day11/input1.txt")
stones = list(map(lambda x: int(x), file.readline().split()))
file.close()

for _ in range(25):
    new_stones: list[int] = []
    
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_stones.append(int(stone_str[:int(len(stone_str)/2)]))
            new_stones.append(int(stone_str[int(len(stone_str)/2):]))
        else:
            new_stones.append(stone * 2024)
            
    stones = new_stones
    
print(len(stones))
