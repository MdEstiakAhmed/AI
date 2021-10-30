roadMap = {
    "arad": { "sibiu": 140, "timisoara": 118, "zerind": 75 },
    "zerind": { "arad": 75, "oradea": 71 },
    "oradea": { "zerind": 71, "sibiu": 151 },
    "timisoara": { "arad": 118, "lugoj": 111 },
    "lugoj": { "timisoara": 111, "mehadia": 70 },
    "mehadia": { "lugoj": 70, "drobeta": 75 },
    "drobeta": { "mehadia": 75, "craiova": 120 },
    "craiova": { "drobeta": 120, "rimnicu": 146, "pitesti": 138, },
    "pitesti": { "craiova": 138, "bucharest": 101, "rimnicu": 97 },
    "rimnicu": { "craiova": 146, "pitesti": 97, "sibiu": 80 },
    "sibiu": { "rimnicu": 80, "oradea": 151, "arad": 140, "fagaras": 99 },
    "fagaras": { "sibiu": 99, "bucharest": 211 }
}


def checkGoal(goal, children):
    flag = False
    for i in range(len(children)):
        if (children[i] == goal):
            flag = True
    return flag


def getSmallNode(listObj):
    length = len(listObj)
    min = float('inf')
    minIndex = 0
    while (length > 0):
        length = length - 1
        value = list(listObj[length].values())[0]
        if (value < min):
            min = value;
            minIndex = length

    return {'key': list(listObj[minIndex].keys())[0], 'value': list(listObj[minIndex].values())[0]};



def checkStack(stack, children):
    newChildren = []
    for childIndex in range(len(children)):
        child = children[childIndex]
        flag = False
        for stackIndex in range(len(stack)):
            stackItem = stack[stackIndex]
            if (child == stackItem):
                flag = True
        if (flag == False):
            newChildren.append(child)
    return newChildren


def mainFunc(map, start, end):
    path = []
    cost = 0
    current = start
    path.append(current)

    while (True):
        currentNodeChildren = list(map[current].keys())
        goalResponse = checkGoal(end, currentNodeChildren)
        if (goalResponse == True):
            path.append(end)
            cost = cost + map[current][end]
            break
        else:
            isAvailableInStack = checkStack(path, currentNodeChildren)
            newList = []
            for i in range(len(isAvailableInStack)):
                newObj = {}
                newObj[isAvailableInStack[i]] = map[current][isAvailableInStack[i]]
                newList.append(newObj)
            
            smallest = getSmallNode(newList)
            current = smallest['key']
            path.append(smallest['key'])
            cost = cost + smallest['value']

    return path, cost

path, cost = mainFunc(roadMap, 'arad', 'bucharest')

print("Path: "," >> ".join(path))
print('Cost: ',cost)