import sys
import time
from dataclasses import dataclass


@dataclass
class BlockGroup:
    content: list[int]
    free: bool
    moved: bool

#-------CODE-------#

def loader(dataFilePath: str):
    
    with open(dataFilePath) as file:
        for line in file:
            lineString = line.rstrip()
    
    return(lineString)
#Function to return puzzle 1 result
def puzzle1(dataFilePath: str):

    line = loader( dataFilePath )
    unCompressed = []
    isFile = 0
    fileID = 0
    for i, char in enumerate(line):
        for _ in range(int(char)):
            if isFile%2 == 0:
                unCompressed.append(fileID)
            else:
                unCompressed.append(-1)
        if isFile%2 == 0:
            fileID += 1
        isFile += 1
    freePointer = 0

    while freePointer < len(unCompressed)-1:
        #print(unCompressed[freePointer])
        if unCompressed[freePointer] == -1:
            unCompressed[freePointer] = unCompressed.pop(-1)
        else:
            freePointer += 1
        #print(len(unCompressed), freePointer)
    total = 0
    for block, id in enumerate(unCompressed):
        if id != -1:
            total += block * id
    print(unCompressed)
    return total

#Function to Return puzzle 2 result
def puzzle2(dataFilePath: str):
    line = loader( dataFilePath )
    unCompressed = []
    isFile = 0
    fileID = 0
    free = False
    for i, char in enumerate(line):
        temp = []

        for _ in range(int(char)):
            if isFile%2 == 0:
                temp.append(fileID)
                free = False
            else:
                temp.append(-1)
                free = True
        if int(char) != 0:        
            unCompressed.append(BlockGroup(temp,free, False))    
        if isFile%2 == 0:
            fileID += 1
        isFile += 1

    for i in range(len(unCompressed)):
        freePointer = 0
        print(len(unCompressed))
        while freePointer < len(unCompressed)-1-i:
            ''''''
            if unCompressed[freePointer].free == True:
                bg = unCompressed[len(unCompressed) - i -1]
                if bg.free == False and bg.moved == False:
                    if len(bg.content) < len(unCompressed[freePointer].content):
                        unCompressed[freePointer].content = unCompressed[freePointer].content[:len(unCompressed[freePointer].content) - len(bg.content)]
                        unCompressed[len(unCompressed) - i -1] = BlockGroup([-1 for _ in range(len(bg.content))], True, False)
                        unCompressed.insert(freePointer, bg)
                        break
                    elif len(bg.content) == len(unCompressed[freePointer].content):
                        unCompressed[len(unCompressed) - i -1] = unCompressed[freePointer]
                        unCompressed[freePointer] = bg
                        break
            
            freePointer += 1
        unCompressed[len(unCompressed) - i -1].moved = True
    
    compressed = []
    for block in unCompressed:
        compressed.extend(block.content)
    total = 0
    for block, id in enumerate(compressed):
        if id != -1:
            total += block * id
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
        print("Part 2:")
        print("      Answer: ", answer)
        print("compute Time: ", computeTime)