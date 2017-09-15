import sys
from general_search import general_search
from node import Node
from path import Path
from utility import getNode
from utility import printLabels
from utility import printResult
from printUtil import printLabels
from printUtil import printLabelsIDS
import utility

def main():
	arg = sys.argv[1]
	filename = str(arg)
	f = open(filename, "r")
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

	# clears output file each time the program runs
	outputFile = open("output.txt", 'w')
	outputFile.write("\tSearch Algorithm Output\n\n")
	outputFile.close()

	startPath = Path(startNode, None, 0)

	printLabels()
	dfsStart = (None, startPath)
	dfsResult = general_search(dfsStart, "dfs")
	#print result

	printLabels()
	bfsStart = (None, startPath)
	bfsResult = general_search(bfsStart, "bfs")

	# depth-limited search with default depth of 2
	printLabels()
	dlsStartPath = Path(startNode, None, 0)
	dlsStartPath.fnValue = 2
	dlsStart = (2, dlsStartPath)
	dlsResult = general_search(dlsStart, "depth_limited")

	printLabels()
	idsStartPath = Path(startNode, None, 0)
	for i in range(1,50):
		printLabelsIDS(i)
		idsStartPath.fnValue = i
		idsStart = (i, idsStartPath)
		idsResult = general_search(idsStart, "iterative_deepening")
		if idsResult is "pass":
			break
	# printResult fn?

	printLabels()
	ucsStart = (0, startPath)
	ucsResult = general_search(ucsStart, "uniform_cost")

	printLabels()
	greedyStart = (startPath.node.heuristic, startPath) 
	greedyResult = general_search(greedyStart, "greedy")

	astarStart = (startPath.node.heuristic, startPath)
	astarResult = general_search(astarStart, "astar")

	printLabels()
	hcStart = (startPath.node.heuristic, startPath)
	hcResult = general_search(hcStart, "hill_climbing")

	printLabels()
	beamStart = (startPath.node.heuristic, startPath)
	beamResult = general_search(beamStart, "beam")


if __name__ == "__main__":
	main()

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