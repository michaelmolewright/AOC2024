import sys
import time

def checkUpdate(update, ruleset) -> bool:
    correct = True
    for i, val in enumerate(update):
        myRules = ruleset[str(val)]
        for followingVals in update[i+1:]:
            if followingVals not in myRules:
                correct = False

    return correct

def reOrder(update, ruleset) -> list[int]:
    #bubble
    for i in range(0, len(update)):
        for j in range(i+1, len(update)):
            if update[i] in ruleset[str(update[j])]:
                temp = update[i]
                update[i] = update[j]
                update[j] = temp

    return update
#-------CODE-------#

def loader(dataFilePath: str):
    part1, part2 = [], []
    top = True
    with open(dataFilePath) as file:
        for line in file:
            lineString = line.rstrip()
            if top:
                if lineString == '':
                    top = False
                else:
                    part1.append([int(i) for i in lineString.split("|")])
            else:
                part2.append([int(i) for i in lineString.split(",")])
    return part1, part2
    
#Function to return puzzle 1 result
def puzzle1(dataFilePath: str):
    rules, updates = loader(dataFilePath)
    ruleset = {}
    for rule in rules:
        if str(rule[0]) in ruleset.keys():
            ruleset[str(rule[0])].append(rule[1])

        else:
            ruleset[str(rule[0])] = [rule[1]]
        
        if str(rule[1]) not in ruleset.keys():
            ruleset[str(rule[1])] = []
    

    total = 0
    for update in updates:
        if checkUpdate(update, ruleset):
            total += update[len(update)//2]


    return total

#Function to Return puzzle 2 result
def puzzle2(dataFilePath: str):
    rules, updates = loader(dataFilePath)
    ruleset = {}

    for rule in rules:
        if str(rule[0]) in ruleset.keys():
            ruleset[str(rule[0])].append(rule[1])

        else:
            ruleset[str(rule[0])] = [rule[1]]
        
        if str(rule[1]) not in ruleset.keys():
            ruleset[str(rule[1])] = []

    total = 0
    for update in updates:
        if not checkUpdate(update, ruleset):
            reOrderedUpdate = reOrder(update, ruleset)
            total += reOrderedUpdate[len(reOrderedUpdate)//2]
    
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