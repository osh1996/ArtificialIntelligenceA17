from node import Node
from utility import getNode

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
			print ("added " + line + " to nodeList")

		else:
			edgeList.append(line)
			print ("added " + line + " to edgeList")

#print (nodeList)
#print (edgeList)
nodeObjects = list()
for item in nodeList:
	current = item.split()
	name = current[0]
	heur = current[1]
	newNode = Node(name, heur)
	nodeObjects.append(newNode)
	print (newNode)

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

	firstNode.add_edge(secondNode, length)
	secondNode.add_edge(firstNode, length)

startNode = getNode("S")

## call all search functions ;)

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