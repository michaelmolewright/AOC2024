filename = "../data/puzzleData/day2.txt"
masterList = []

with open(filename) as file:
    for line in file:
        lineString = line.rstrip()
        numbers = [int(i) for i in lineString.split(" ")]
        masterList.append(numbers)

def isSafe(report) -> bool:
    differences = []
    for i in range(0, len(report) - 1):
        diff = report[i+1] - report[i]
        differences.append(diff)
    
    sign = 1
    if differences[0] < 0:
        sign = -1
    
    for difs in differences:
        if difs/sign <= 0 or abs(difs) not in [1,2,3]:
            return False

    return True

def puzzle1(masterList):
    safeReports = 0
    for row in masterList:
        if isSafe(row):
            safeReports += 1
    return safeReports

def puzzle2(masterList):#SLOW
    safeReports = 0
    for row in masterList:
        if isSafe(row):
            safeReports += 1
        else:
            notSafe = True
            index = 0
            while notSafe and index < len(row):
                savedItem = row.pop(index)
                if isSafe(row):
                    safeReports += 1
                    notSafe = False
                else:
                    row.insert(index, savedItem)
                    index += 1
    return safeReports

print(puzzle1(masterList))
print(puzzle2(masterList))
