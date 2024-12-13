import sys
import time

class Lab():
    def __init__(self):
        self.guardDir = 0
        self.obsticlesX = []
        self.obsticlesY = []
        self.walked = []
        self.states = []
        self.possibleObsticles = []
    
    def setDimensions(self,width, height):
        self.width = width
        self.height = height
        for i in range(0, width):
            self.obsticlesX.append([])
        for j in range(0, height):
            self.obsticlesY.append([])
    
    def addObsticle(self, x, y):
        self.obsticlesX[x].append(y)
        self.obsticlesY[y].append(x)

    def removeObsticle(self, x, y):
        self.obsticlesX[x].remove(y)
        self.obsticlesY[y].remove(x)

    def setGuardLoc(self,x,y):
        self.guardLocX = x
        self.guardLocY = y
        self.leftLab = False
    
    def saveState(self):
        if (self.guardLocX,self.guardLocY) not in self.walked:
            self.walked.append( (self.guardLocX,self.guardLocY) )
        if (self.guardLocX,self.guardLocY, self.guardDir) not in self.states:
            self.states.append( (self.guardLocX,self.guardLocY, self.guardDir) )
            
    
    def walk(self):
        hitObsticle = False
        if self.leftLab:
            print("Guard has left!!")
        else:
            if self.guardDir == 0: #up Human View
                while not hitObsticle:
                    if self.guardLocY - 1 in self.obsticlesX[self.guardLocX]:
                        hitObsticle = True
                        self.saveState()
                    elif self.guardLocY == 0:
                        self.leftLab = True
                        hitObsticle = True
                        self.saveState()
                    else:
                        self.guardLocY -= 1
                        self.saveState()

            elif self.guardDir == 1:
                while not hitObsticle:
                    if self.guardLocX + 1 in self.obsticlesY[self.guardLocY]:
                        hitObsticle = True
                        self.saveState()
                    elif self.guardLocX == self.width -1:
                        self.leftLab = True
                        hitObsticle = True
                        self.saveState()
                    else:
                        self.guardLocX += 1
                        self.saveState()

            elif self.guardDir == 2:
                while not hitObsticle:
                    if self.guardLocY + 1 in self.obsticlesX[self.guardLocX]:
                        hitObsticle = True
                        self.saveState()
                    elif self.guardLocY == self.height -1:
                        self.leftLab = True
                        hitObsticle = True
                        self.saveState()
                    else:
                        self.guardLocY += 1
                        self.saveState()
                        
            elif self.guardDir == 3:
                while not hitObsticle:
                    if self.guardLocX - 1 in self.obsticlesY[self.guardLocY]:
                        hitObsticle = True
                        self.saveState()
                    elif self.guardLocX == 0:
                        self.leftLab = True
                        hitObsticle = True
                        self.saveState()
                    else:
                        self.guardLocX -= 1
                        self.saveState()

            self.guardDir = (self.guardDir + 1)%4
    
    def walkWithoutSave(self):
        hitObsticle = False

        if self.guardDir == 0: #up Human View
            while not hitObsticle:
                if self.guardLocY - 1 in self.obsticlesX[self.guardLocX]:
                    hitObsticle = True
                elif self.guardLocY == 0:
                    self.leftLab = True
                    hitObsticle = True
                else:
                    self.guardLocY -= 1
        elif self.guardDir == 1:
            while not hitObsticle:
                if self.guardLocX + 1 in self.obsticlesY[self.guardLocY]:
                    hitObsticle = True
                elif self.guardLocX == self.width - 1:
                    self.leftLab = True
                    hitObsticle = True
                else:
                    self.guardLocX += 1
        elif self.guardDir == 2:
            while not hitObsticle:
                if self.guardLocY + 1 in self.obsticlesX[self.guardLocX]:
                    hitObsticle = True
                elif self.guardLocY == self.height -1:
                    self.leftLab = True
                    hitObsticle = True
                else:
                    self.guardLocY += 1
        elif self.guardDir == 3:
            while not hitObsticle:
                if self.guardLocX - 1 in self.obsticlesY[self.guardLocY]:
                    hitObsticle = True
                elif self.guardLocX == 0:
                    self.leftLab = True
                    hitObsticle = True
                else:
                    self.guardLocX -= 1

        self.guardDir = (self.guardDir + 1)%4

    def countObsticles(self):
        count = 0
        for i in self.obsticlesX:
            for j in i:
                count +=1 
        for i in self.obsticlesY:
            for j in i:
                count +=1 
        return count

    def walkCheckingObsticles(self, checkStates, initPos):
        self.workingObsticles = []

        for i in range(1,len(checkStates)):
            if initPos != (checkStates[i][0],checkStates[i][1]):
                currentTrace = [ (s[0],s[1]) for s in checkStates[:i]]
                self.leftLab = False
                self.guardLocX = checkStates[i-1][0]
                self.guardLocY = checkStates[i-1][1]
                self.guardDir = (checkStates[i-1][2] + 1) %4
                
                if ( (checkStates[i][0],checkStates[i][1]) not in currentTrace):
                    self.addObsticle(checkStates[i][0],checkStates[i][1])
                    

                    seenStates = []
                    
                    while not self.leftLab:
                        
                        if (self.guardLocX, self.guardLocY, self.guardDir) in seenStates:

                            if (checkStates[i][0],checkStates[i][1]) not in self.workingObsticles:
                                self.workingObsticles.append( (checkStates[i][0],checkStates[i][1]) )
                            break
                        seenStates.append((self.guardLocX, self.guardLocY, self.guardDir))

                        self.walkWithoutSave()

                    self.removeObsticle(checkStates[i][0],checkStates[i][1])
                

#-------CODE-------#

def loader(dataFilePath: str) -> Lab:
    labMap = []
    with open(dataFilePath) as file:
        for line in file:
            lineString = line.rstrip()
            labMap.append(lineString)

    myLab = Lab()
    myLab.setDimensions(len(labMap[0]), len(labMap))

    for i, row in enumerate(labMap):
        for j, item in enumerate(row):
            if item == '#':
                myLab.addObsticle(j,i)
            elif item == '^':
                myLab.setGuardLoc(j,i)
    return myLab

#Function to return puzzle 1 result
def puzzle1(dataFilePath: str):
    myLab = loader(dataFilePath)
    myLab.saveState()
    while not myLab.leftLab:
        myLab.walk()
    print(myLab.states)
    return len(myLab.walked)

#Function to Return puzzle 2 result
def puzzle2(dataFilePath: str): #rectangles
    myLab = loader(dataFilePath)
    initPos = (myLab.guardLocX, myLab.guardLocX)
    while not myLab.leftLab:
        myLab.walk()
    
    myLab.walkCheckingObsticles(myLab.states, initPos)
    return len(myLab.workingObsticles)



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