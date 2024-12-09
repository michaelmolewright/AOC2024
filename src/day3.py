import sys
import time

#-------CODE-------#

def loader(dataFilePath: str):
    fullString = ''
    with open(dataFilePath) as file:
        for line in file:
            lineString = line.rstrip()
            fullString += lineString + '\n'
    return fullString

#Function to return puzzle 1 result
def puzzle1(dataFilePath: str):

    potentialVals = []
    input = loader(dataFilePath)
    for i in range(0, len(input)):
        if input[i:i+4] == 'mul(':
            for j in range(3,9):
                if j + i + 4 > len(input):
                    break
                if input[j + i + 4] == ')':
                    potentialVals.append(input[i+4:j + i + 4])
                    break
    
    total = 0
    for val in potentialVals:
        split = val.split(",")
        valid = True
        if len(split) == 2:
            for i in val:
                if i not in ["1", "2",'3','4','5','6','7','8','9','0',',']:
                    valid = False
            if valid:
                total += int(split[0]) * int(split[1])

    return total

#Function to Return puzzle 2 result
def puzzle2(dataFilePath: str):
    potentialVals = []
    input = loader(dataFilePath)
    enabled=True
    for i in range(0, len(input)):
        if input[i:i+4] == 'do()':
            enabled = True
        if input[i:i+7] == "don't()":
            enabled = False
        if input[i:i+4] == 'mul(' and enabled:
            for j in range(3,9):
                if j + i + 4 > len(input):
                    break
                if input[j + i + 4] == ')':
                    potentialVals.append(input[i+4:j + i + 4])
                    break
    
    total = 0
    for val in potentialVals:
        split = val.split(",")
        valid = True
        if len(split) == 2:
            for i in val:
                if i not in ["1", "2",'3','4','5','6','7','8','9','0',',']:
                    valid = False
            if valid:
                total += int(split[0]) * int(split[1])

    return total
    return "Not Implemented"



#------BOILERPLATE------#

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print("You Need to specify 2 arguments.\n\nPuzzle: 1, 2\nData: test, real")
        exit(1)
    
    dataPath = args[0][:-3] + '.txt'
    day = args[0][:-3]

    fullPath = ''
    if args[2].lower() == 'test':
        fullPath = "../data/testData/" + dataPath

    elif args[2].lower() == 'real':
        fullPath = "../data/realData/" + dataPath
    else:
        print("%s argument not recognised as a valid data type", args[2])
        exit(1)

    if args[1] == '1':

        start = time.time()
        answer = puzzle1(fullPath)
        end = time.time()
        computeTime = end - start

        print("\n\n---------------", day, "---------------")
        print("Part 1:")
        print("      Answer: ", answer)
        print("compute Time: ", computeTime)
        print("\n\n")
    elif args[1] == '2':
        start = time.time()
        answer = puzzle2(fullPath)
        end = time.time()
        computeTime = end - start

        print("\n\n---------------", day, "---------------")
        print("Part 1:")
        print("      Answer: ", answer)
        print("compute Time: ", computeTime)
        print("\n\n")

    