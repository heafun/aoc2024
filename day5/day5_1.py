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

page_sum = 0

for update in updates:
    correct = True
    
    for i in range(len(update) - 1):
        page1 = update[i]
        page2 = update[i+1]
        
        if any(list(map(lambda rule: rule[0] == page1 and rule[1] == page2, rules))):
            continue
        elif any(list(map(lambda rule: rule[1] == page1 and rule[0] == page2, rules))):
            correct = False
            break
        else:
            print('Missing Rule: ' + page1 + '|' + page2)
        
    if correct:
        page_sum += int(update[int((len(update) - 1) / 2)])
        
print(page_sum)
