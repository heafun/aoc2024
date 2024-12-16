file = open("day1/input1.txt")
lines = file.readlines()
file.close()

list1 = []
list2 = []

for line in lines:
    line_parts = line.split()
    list1.append(line_parts[0])
    list2.append(line_parts[1])
    
list1.sort()
list2.sort()

sum = 0

for i in range(len(list1)):
    sum += abs(int(list1[i]) - int(list2[i]))
    
print(sum)
