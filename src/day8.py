import sys
import time

#-------CODE-------#

def loader(dataFilePath: str):
    data = {}
    data["height"] = 0
    data["antennas"] = {}
    with open(dataFilePath) as file:
        for y, line in enumerate(file):
            lineString = line.rstrip()
            for x, char in enumerate(lineString):
                if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 57):    
                    if char in data["antennas"].keys():
                        data["antennas"][char].append( (x,y) )
                    else:
                        data["antennas"][char] = [ (x,y) ]

            
            data["height"] += 1
        data["width"] = len(lineString)
    
    return data

def inBounds( location, width, height):
    xIn = False
    yIn = False
    if location[0] >= 0 and location[0] < width:
        xIn = True
    if location[1] >= 0 and location[1] < height:
        yIn = True
    if xIn and yIn:
        return True
    return False

def gcd(a: int, b: int) -> int: #NOT MY CODE - just wanted the cleanest gcd
    while b:
        a, b = b, a%b
    return a
#Function to return puzzle 1 result
def puzzle1(dataFilePath: str):
    data = loader(dataFilePath)
    antinodes = []
    for ant in data["antennas"].keys():
        for i in range( len(data["antennas"][ant]) - 1 ):
            for j in range(i+1, len(data["antennas"][ant])):
                x_diff = data["antennas"][ant][j][0] - data["antennas"][ant][i][0]
                y_diff = data["antennas"][ant][j][1] - data["antennas"][ant][i][1]
                loc1 = (data["antennas"][ant][j][0] - (2 * x_diff), data["antennas"][ant][j][1] - (2 * y_diff))
                loc2 = (data["antennas"][ant][j][0] + x_diff, data["antennas"][ant][j][1] + y_diff)
                
                if inBounds( loc1, data["width"], data["height"]):
                    antinodes.append(loc1)
                if inBounds( loc2, data["width"], data["height"]):
                    antinodes.append(loc2)
    
    antinodes = list(dict.fromkeys(antinodes))
    return len(antinodes)

#Function to Return puzzle 2 result
def puzzle2(dataFilePath: str):
    data = loader(dataFilePath)
    antinodes = []
    for ant in data["antennas"].keys():
        for i in range( len(data["antennas"][ant]) - 1 ):
            for j in range(i+1, len(data["antennas"][ant])):
                x_diff = data["antennas"][ant][j][0] - data["antennas"][ant][i][0]
                y_diff = data["antennas"][ant][j][1] - data["antennas"][ant][i][1]
                divisor = gcd(x_diff, y_diff)
                x_diff = int(x_diff/divisor)
                y_diff = int(y_diff/divisor)

                antinodes.append( (data["antennas"][ant][i][0], data["antennas"][ant][i][1]) )
                antinodes.append( (data["antennas"][ant][j][0], data["antennas"][ant][j][1]) )

                loc1 = [data["antennas"][ant][j][0] - x_diff, data["antennas"][ant][j][1] - y_diff]
                while inBounds( loc1, data["width"], data["height"]):
                    antinodes.append( (loc1[0], loc1[1]) )
                    loc1[0] -= x_diff
                    loc1[1] -= y_diff
                
                loc2 = [data["antennas"][ant][j][0] + x_diff, data["antennas"][ant][j][1] + y_diff]
                while inBounds( loc2, data["width"], data["height"]):
                    antinodes.append( (loc2[0], loc2[1]) )
                    loc2[0] += x_diff
                    loc2[1] += y_diff

    antinodes = list(dict.fromkeys(antinodes))
    return len(antinodes)



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