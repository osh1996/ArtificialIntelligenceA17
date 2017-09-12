from node import Node
from utility import getNode
from utility import printLabels
from utility import printResult
import utility
import depthFirstSearch
import breadthFirstSearch
import depthLimitSearch
import iterativeDeepeningSearch
import uniformCostSearch
import greedySearch
import aStarSearch
import beamSearch
import hillClimbingSearch

f = open("graph.txt", "r")
nodeList = list()
edgeList = list()

q = list()
flag = 0
for line in f:
	if "#" in line:
		flag = 1
	else:
		if flag == 1:
			nodeList.append(line)

		else:
			edgeList.append(line)
f.close()

#print (nodeList)
#print (edgeList)
nodeObjects = list()
for item in nodeList:
	current = item.split()
	name = current[0]
	heur = float(current[1])
	newNode = Node(name, heur)
	nodeObjects.append(newNode)
	print (newNode)

startNode = getNode("S", nodeObjects)
goalNode = Node("G", 0)
nodeObjects.append(goalNode)

for item in edgeList:
	current = item.split()
	firstNodeName = current[0]
	secondNodeName = current[1]
	length = current[2]

	firstNode = 0
	secondNode = 0
	for node in nodeObjects:
		if node.name is firstNodeName:
			firstNode = node
		if node.name is secondNodeName:
			secondNode = node

	firstNode.add_edge(secondNode, float(length))
	secondNode.add_edge(firstNode, float(length))

outputFile = open("output.txt", 'w')
outputFile.write("\tSearch Algorithm Output\n\n")
outputFile.close()

dfs = depthFirstSearch.depthFirstSearch(startNode, goalNode)
dfsResult = dfs.depthFirstSearchFn()
printResult(dfsResult)

bfs = breadthFirstSearch.breadthFirstSearch(startNode, goalNode)
bfsResult = bfs.breadthFirstSearchFn()
printResult(bfsResult)

dlsLimit = 2
dls = depthLimitSearch.depthLimitSearch(startNode, goalNode, dlsLimit)		
dlsResult = dls.depthLimitSearchFn()
printResult(dlsResult)

ids = iterativeDeepeningSearch.iterativeDeepeningSearch(startNode, goalNode)
idsResult = ids.iterativeDeepeningSearchFn()
printResult(idsResult)

ucs = uniformCostSearch.uniformCostSearch(startNode, goalNode)
ucsResult = ucs.uniformCostSearchFn()
printResult(ucsResult)

greedy = greedySearch.greedySearch(startNode, goalNode)
greedyResult = greedy.greedySearchFn()
printResult(greedyResult)

astar = aStarSearch.aStarSearch(startNode, goalNode)
astarResult = astar.aStarSearchFn()
printResult(astarResult)

hcs = hillClimbingSearch.hillClimbingSearch(startNode, goalNode)
hcsResult = hcs.hillClimbingSearchFn()
printResult(hcsResult)

beam = beamSearch.beamSearch(startNode, goalNode)
beamResult = beam.beamSearchFn()
printResult(beamResult)


#Depth 1st Search
#Chris
#Breath 1st Search
#Tung
#Depth-limited Search Depth-limit-2
#David
#Iterative Deepening Search showing all iterations
#Chris
#Uniform Cost Search
#Tung
#Greedy Search
#David
#A*
#Chris
#Hill-climbing
#David
#Beam Search W=2
#Tung