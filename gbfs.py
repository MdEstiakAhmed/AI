SLD = {
    "arad": { "distance": 366 },
    "bucharest": { "distance": 0 },
    "craiova": { "distance": 160 },
    "drobeta": { "distance": 242 },
    "eforie": { "distance": 160 },
    "fagaras": { "distance": 176 },
    "giurgiu": { "distance": 77 },
    "hirsova": { "distance": 151 },
    "lasi": { "distance": 226 },
    "lugoj": { "distance": 244 },
    "mehadia": { "distance": 241 },
    "neamt": { "distance": 234 },
    "oradea": { "distance": 380 },
    "pitesti": { "distance": 100 },
    "rimnicu": { "distance": 193 },
    "sibiu": { "distance": 253 },
    "timisoara": { "distance": 329 },
    "urziceni": { "distance": 80 },
    "vaslui": { "distance": 199 },
    "zerind": { "distance": 374 }
}

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

def getMin(child):
    l = len(child)
    min = float('inf')
    minObject = {}
    while (l > 0):
        l = l - 1
        if (child[l]['value'] < min):
            min = child[l]['value'];
            minObject = child[l];
    return minObject;

def mainFunc(start, end):
    path = [start]
    cost = 0
    pathValueList = []
    current = start
    while (True):
        if (current != end):
            expandAreaList = list(roadMap[current].keys())
            expandAreaValueList = []
            for index in range(len(expandAreaList)):
                expandAreaValueList.append({"area": expandAreaList[index],"value": SLD[expandAreaList[index]]['distance'],"pathCost": roadMap[current][expandAreaList[index]]})
            smallArea = getMin(expandAreaValueList)
            pathValueList.append(smallArea["pathCost"])
            path.append(smallArea["area"]);
            cost = cost + smallArea["pathCost"]
            current = smallArea["area"]
        else:
            break
    return cost, path

cost, path = mainFunc('arad', 'bucharest')

print("path: "," >> ".join(path))
print("cost: ",cost)