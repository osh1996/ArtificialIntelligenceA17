import sys
from general_search import general_search
from node import Node
from path import Path
from utility import getNode
from printUtil import printLabels
from printUtil import printLabelsIDS
from printUtil import printResult

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
				if line.strip() != "":
					nodeList.append(line)

			else:
				if line.strip() != "":
					edgeList.append(line)
	f.close()

	nodeObjects = list()
	for item in nodeList:
		current = item.split()
		name = current[0]
		heur = float(current[1])
		newNode = Node(name, heur)
		nodeObjects.append(newNode)

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
	outputFile = open("output.txt", 'a')

	startPath = Path(startNode, None, 0)

	printLabels("dfs")
	dfsStart = (None, startPath)
	dfsResult = general_search(dfsStart, "dfs")
	printResult(dfsResult)

	printLabels("bfs")
	bfsStart = (None, startPath)
	bfsResult = general_search(bfsStart, "bfs")
	printResult(bfsResult)

	# depth-limited search with default depth of 2
	printLabels("depth_limited")
	dlsStartPath = Path(startNode, None, 0)
	dlsStartPath.fnValue = 2
	dlsStart = (2, dlsStartPath)
	dlsResult = general_search(dlsStart, "depth_limited")
	printResult(dlsResult)

	idsStartPath = Path(startNode, None, 0)
	idsResult = -1
	for i in range(0,50):
		printLabelsIDS(i)
		idsStartPath.fnValue = i
		idsStart = (i, idsStartPath)
		idsResult = general_search(idsStart, "depth_limited")
		if idsResult is "pass":
			break
	printResult(idsResult)

	printLabels("uniform_cost")
	ucsStart = (0, startPath)
	ucsResult = general_search(ucsStart, "uniform_cost")
	printResult(ucsResult)

	printLabels("greedy")
	greedyStart = (startPath.node.heuristic, startPath) 
	greedyResult = general_search(greedyStart, "greedy")
	printResult(greedyResult)

	printLabels("astar")
	astarStart = (startPath.node.heuristic, startPath)
	astarResult = general_search(astarStart, "astar")
	printResult(astarResult)

	printLabels("hill_climbing")
	hcStart = (startPath.node.heuristic, startPath)
	hcResult = general_search(hcStart, "hill_climbing")
	printResult(hcResult)

	printLabels("beam")
	beamStart = (startPath.node.heuristic, startPath)
	beamResult = general_search(beamStart, "beam")
	printResult(beamResult)


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