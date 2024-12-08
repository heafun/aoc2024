file = open("day7/input1.txt")
lines = list(map(lambda x: x.strip(), file.readlines()))
file.close()

def concat(value1: int, value2: int):
    return int(str(value1) + str(value2))

def solve(value: int, values: list[int], result: int) -> bool:
    if len(values) == 1:
        if value * values[0] == result \
            or value + values[0] == result \
            or concat(value, values[0]) == result:
            return True
        
        return False
    else:
        return solve(value * values[0], values[1:], result) \
            or solve(value + values[0], values[1:], result) \
            or solve(concat(value, values[0]), values[1:], result)
                
        
calibration_result = 0

for line in lines:
    result = int(line.split()[0][:-1])
    values = list(map(lambda x: int(x), line.split()[1:]))
    
    calibration_result += result if solve(values[0], values[1:], result) else 0
    
print(calibration_result)
