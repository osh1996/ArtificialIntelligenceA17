from Queue import PriorityQueue

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
	labels = "\tExpanded\tQueue\nL=" + limit + "\t"
	file.write(labels)
	file.close()

def printQueueState(queue):
	file = open("output.txt", 'a')
	if(queue):
		expandedNode = queue.get_nowait()
		nodeName = expandedNode[1].node.name
		queue.put_nowait(expandedNode)

	outputText = nodeName + "\t\t["
	newQueue = PriorityQueue(maxsize=0)

	while (not queue.empty()):
		queueTuple = queue.get_nowait()
		print(queueTuple[0])
		if(queueTuple[0] != -1):
			outputText += queueTuple[0]
		printPrevNodes(queueTuple[1])
		newQueue.put_nowait(queueTuple)

	outputText += "]\n"
	file.write(outputText)
	file.close()
	return newQueue

def printPrevNodes(currQueueItem):
	file = open("output.txt", 'a')
	outputText = "<" + currQueueItem.node.name
	
	currNode = currQueueItem.prevNode
	while(currNode != -999):
		outputText = outputText + "," + currNode.node.name
		currNode = currNode.prevNode
	
	outputText = outputText + "> "
	file.write(outputText)
	file.close()

def printResult(result):
	file = open("output.txt", 'a')
	if(result == "G"):
		file.write("\t\tgoal reached!\n\n\n")
	else:
		file.write("\n\n\n")

