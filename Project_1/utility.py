from Queue import PriorityQueue
from node import Node

def getNode(name, nodeObjects):
	for node in nodeObjects:
		if name == node.name:
			return node
	return -1

	## prints labels for search outcome
def printLabels():
	file = open("output.txt", 'a')
	file.write("\tExpanded\tQueue\n\t\t")
	file.close()

	## print labels for Iterative Deepening (displays current iteration)
def printLabelsIDS(limit):
	file = open("output.txt", 'a')
	labels = "\tExpanded\tQueue\nL=" + str(limit) + "\t"
	file.write(labels)
	file.close()

def printQueueState(queue):
	file = open("output.txt", 'a')
	queueAsList = list(queue.queue)
	firstElt = 1
	for currQueueTuple in queueAsList:
		if firstElt:
			file.write(currQueueTuple[1].node.name + "\t\t[")
			firstElt = 0
		if currQueueTuple[0] > -1:
			file.write(str(currQueueTuple[0]))
		printPath(currQueueTuple)

	file.close()
	return newQueue

def printPath(currQueueTuple):
	file = open("output.txt", 'a')
	file.write("<" + currQueueTuple[1].node.name)

	currItem = currQueueTuple[1].prevNode
	while currItem is not None:
		file.write("," + currItem[1].node.name)
		currItem = currItem[1].prevNode
	file.write(">")
	file.close()

def printResult(result):
	file = open("output.txt", 'a')
	if(result == "G"):
		file.write("\t\tgoal reached!\n\n\n")
	else:
		file.write("\n\n\n")

