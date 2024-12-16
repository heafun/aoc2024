def is_safe(levels: list) -> bool:
    is_increment = levels[0] < levels[-1]        
    
    for i in range(len(levels) - 1):
        delta = abs(levels[i] - levels[i + 1])
            
        if delta < 1 or delta > 3:
            return False
        
        if is_increment:
            if levels[i] > levels[i + 1]:
                return False
        else:
            if levels[i] < levels[i + 1]:
                return False            
            
    return True
        
# Start
file = open("day2/input1.txt")
lines = file.readlines()
file.close()

safe_count = 0

for line in lines:
    levels = list(map(int, line.split()))        
    safe_count += 1 if is_safe(levels) else 0
    
print(safe_count)
