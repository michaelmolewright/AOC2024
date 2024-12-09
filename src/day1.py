filename = "../data/puzzleData/day1.txt"
list1 = []
list2 = []

with open(filename) as file:
    for line in file:
        lineString = line.rstrip()
        numbers = lineString.split("   ")
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

list1.sort()
list2.sort()

puzzleAnswer1 = 0

for i in range(0, len(list1)):
    puzzleAnswer1 += abs(list1[i] - list2[i])

print("Answer to Puzzle 1: ", puzzleAnswer1)

puzzleAnswer2 = 0
for i in range(0, len(list1)):
    puzzleAnswer2 += list1[i] * list2.count(list1[i])

print("Answer to Puzzle 2: ", puzzleAnswer2)
