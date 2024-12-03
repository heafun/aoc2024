from enum import Enum


class ValidChars(Enum):
    M = 1
    U = 2
    L = 3
    Open = 4
    NumberPart1 = 5
    NumberOrComma = 6
    NumberPart2 = 7
    NumberOrClose = 8
    
def extractEnabledParts(instructions: str) -> str:
    enabled_instructions = ''
    
    split_instructions = instructions.split('don\'t()')
    
    enabled_instructions += split_instructions[0]
    del split_instructions[0]
    
    for instruction_part in split_instructions:
        instruction_part = instruction_part.removesuffix('do()')
        
        if 'do()' not in instruction_part:
            continue
        
        enabled_instructions += ''.join(instruction_part.split('do()')[1:])
    
    return enabled_instructions

file = open("day3/input1.txt")
lines = file.readlines()
file.close()

instructions = ''.join(lines)

instructions = extractEnabledParts(instructions)

expectedChar = ValidChars.M
instruction = ''
result = 0

for char in instructions:    
    if expectedChar == ValidChars.M:
        instruction = ''
    
    match expectedChar:
        case ValidChars.M:
            if char == 'm':
                expectedChar = ValidChars.U
        case ValidChars.U:
            if char == 'u':
                expectedChar = ValidChars.L
            else:
                expectedChar = ValidChars.M
        case ValidChars.L:
            if char == 'l':
                expectedChar = ValidChars.Open
            else:
                expectedChar = ValidChars.M
        case ValidChars.Open:
            if char == '(':
                expectedChar = ValidChars.NumberPart1
            else:
                expectedChar = ValidChars.M
        case ValidChars.NumberPart1:
            if char.isdigit():
                expectedChar = ValidChars.NumberOrComma
                instruction += char
            else:
                expectedChar = ValidChars.M
        case ValidChars.NumberOrComma:
            if char.isdigit():
                instruction += char
            elif char == ',':
                expectedChar = ValidChars.NumberPart2
                instruction += char
            else:
                expectedChar = ValidChars.M
        case ValidChars.NumberPart2:
            if char.isdigit():
                expectedChar = ValidChars.NumberOrClose
                instruction += char
            else:
                expectedChar = ValidChars.M
        case ValidChars.NumberOrClose:
            if char.isdigit():
                instruction += char
            elif char == ')':
                factors = list(map(int, instruction.split(',')))
                result += factors[0] * factors[1]
                expectedChar = ValidChars.M
            else:
                expectedChar = ValidChars.M
                
print(result)

