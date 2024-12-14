import sys
import time

def check1(answer: int,  values: list[int]) -> bool:
    if len(values) == 2:
        if values[0] + values[1] == answer or values[0] * values[1] == answer:
            return True
        else:
            return False
    else:
        x = check1(answer/values[-1], values[:-1])
        y = check1(answer-values[-1], values[:-1])

        if x or y:
            return True
        else:
            return False

def check2(answer: int,  values: list[int]) -> bool:
    if len(values) == 2:
        if values[0] + values[1] == answer or values[0] * values[1] == answer or str(values[0]) + str(values[1]) == str(answer):
            return True
        else:
            return False
    elif(answer < 0):
        return False
    else:
        
        if answer % values[-1] == 0:
            x = check2(answer//values[-1], values[:-1])
        else:
            x = False
        y = check2(answer-values[-1], values[:-1])
        
        if str(answer)[-len(str(values[-1])):] == str(values[-1]) and len(str(answer)) != len(str(values[-1])):
            z = check2(int(str(answer)[:-len(str(values[-1]))]), values[:-1])
        else:
            z = False

        if x or y or z:
            return True
        else:
            return False

#-------CODE-------#

def loader(dataFilePath: str, puzzle1: bool):
    total = 0
    with open(dataFilePath) as file:
        for line in file:
            lineString = line.rstrip()
            temp = lineString.split(":")
            answer = int(temp[0])
            values = [int(i) for i in temp[1][1:].split(" ")]
            
            if puzzle1:
                if (check1(answer, values)):
                    total += answer
            else:
                if (check2(answer, values)):
                    total += answer
    return total

#Function to return puzzle 1 result
def puzzle1(dataFilePath: str):
    answer = loader(dataFilePath, True)
    return answer

#Function to Return puzzle 2 result
def puzzle2(dataFilePath: str):
    answer = loader(dataFilePath, False)
    return answer



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

        print("---------------", day, "---------------")
        print("Part 1:")
        print("      Answer: ", answer)
        print("compute Time: ", computeTime)

    elif args[1] == '2':
        start = time.time()
        answer = puzzle2(fullPath)
        end = time.time()
        computeTime = end - start

        print("---------------", day, "---------------")
        print("Part 2:")
        print("      Answer: ", answer)
        print("compute Time: ", computeTime)