file = open("day5/input1.txt")
lines = list(map(lambda x: x.strip(), file.readlines()))
file.close()

rules = []
updates = []

rule_section = True

for line in lines:
    if len(line.strip()) == 0:
        rule_section = False
        continue
    
    if rule_section:
        rules.append(line.split('|'))
    else:
        updates.append(line.split(','))
        

def getIncorrectUpdateValue(update: list[str], depth: int = 0) -> int:
    for i in range(len(update) - 1):
        page1 = update[i]
        page2 = update[i+1]
        
        if any(list(map(lambda rule: rule[0] == page1 and rule[1] == page2, rules))):
            continue
        elif any(list(map(lambda rule: rule[1] == page1 and rule[0] == page2, rules))):
            reordered_update = update.copy()
            
            reordered_update[i] = update[i+1]
            reordered_update[i+1] = update[i]
            
            return getIncorrectUpdateValue(reordered_update, depth + 1)
        else:
            print('Missing Rule: ' + page1 + '|' + page2)
            
    if depth > 0:
        return int(update[int((len(update) - 1) / 2)])
    
    return 0


page_sum = 0

for update in updates:
    page_sum += getIncorrectUpdateValue(update)
        
print(page_sum)
