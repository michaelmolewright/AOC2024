import sys
import time



def createWordList(initList: list[str]) -> list[str]:
    allStrings: list[str] = []
    allStrings.extend(initList)
    width = len(initList[0])
    height = len(initList)
    verticalStrings = []
    diagonalStrings1 = []
    diagonalStrings2 = []
    
    for i in range(0, width):
        verticalStrings.append(''.join(string[i] for string in initList))
    
    allStrings.extend(verticalStrings)

    smallerSide = min(height, width)
    start = (0,height)
    end = (width, 0)
    inc = (1,1)
    
    for i in range(0,width):
        diagonalStrings1.append(''.join(initList[j][i+j] for j in range(0,smallerSide-i)))
        diagonalStrings2.append(''.join(initList[height - j-1][(i+j)] for j in range(0,smallerSide-i)))
    
    for i in range(0,height):
        diagonalStrings1.append(''.join(initList[i+j][j] for j in range(0,smallerSide-i)))
        diagonalStrings2.append(''.join(initList[j][width - (i+j) -1] for j in range(0,smallerSide-i))[::-1])
    diagonalStrings1.pop(0)
    diagonalStrings2.pop(0)
    allStrings.extend(diagonalStrings1)
    allStrings.extend(diagonalStrings2)
    return allStrings

def countOccurances(word, string):
    wordlen = len(word)
    number = 0
    for i in range(0, len(string) - wordlen+1):
        if word == string[i:i+wordlen]:
            number += 1
        
    return number

def checkCorners(input, x,y):
    topLeft = input[y-1][x-1]
    topRight = input[y-1][x+1]
    bottomLeft = input[y+1][x-1]
    bottomRight = input[y+1][x+1]

    word1 = topLeft + bottomRight
    word2 = topRight + bottomLeft

    if word1 in ["MS", "SM"] and word2 in ["MS", "SM"]:
        return True
    else:
        return False



#-------CODE-------#

def loader(dataFilePath: str):
    mappedChars = []
    with open(dataFilePath) as file:
        for line in file:
            lineString = line.rstrip()
            mappedChars.append(lineString)
    return mappedChars

#Function to return puzzle 1 result
def puzzle1(dataFilePath: str):
    input = loader(dataFilePath)
    word = 'XMAS'
    wordbackwards = 'SAMX'
    width = len(input[0])
    height = len(input)
    total = 0
    strings = createWordList(input)
    for i in strings:
        j = countOccurances(word, i) + countOccurances(wordbackwards, i)

        total += j

    return total

#Function to Return puzzle 2 result
def puzzle2(dataFilePath: str):
    input = loader(dataFilePath)
    total = 0
    for y in range(1,len(input)-1):
        for x in range(1,len(input[0]) - 1):
            if input[y][x] == 'A':
                if checkCorners(input, x,y):
                    total += 1

                

    return total



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
        print("Part 1:")
        print("      Answer: ", answer)
        print("compute Time: ", computeTime)


    