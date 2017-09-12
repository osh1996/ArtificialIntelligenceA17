from queueItem import QueueItem
from utility import printQueueState
from node import Node
from Queue import PriorityQueue

	# returns a set of all outgoing edges from a given node
def expand(node):
	possibleMoves = list()
	for edge in node.edges:
		adjacentNode = edge[0]
		possibleMoves.append(adjacentNode)
	return possibleMoves

	# calculates f(n) for the given node in the search based on the algorithm used
def calculateValue(queueItem, searchMethod):
	output = -1
	if searchMethod == "depth limited":
		output = (queueItem.prevNode[0]) - 1
	if searchMethod == "uniform cost":
		output = queueItem.pathCost
	if searchMethod == "greedy":
		output = queueItem.node.heuristic
	if searchMethod == "astar":
		output = queueItem.node.heuristic + queueItem.pathCost
	if searchMethod == "beam":
		output = queueItem.node.heuristic
	if searchMethod == "hill climbing":
		output = queueItem.node.heuristic
	return output


def generalSearch(method, initQueue):
	goalNodeName = "G"
	queue = initQueue
	while(queue):
		currQueueTuple = queue.get()
		currQueueItem = currQueueTuple[1]
		print(currQueueItem.node.name)
		if currQueueItem.node.name == goalNodeName:
			return "G"
		openedNodes = expand(currQueueItem.node)
		for action in openedNodes:
			if method != "depth limited" or currQueueTuple[0] != 0:
				totalPathCost = currQueueItem.pathCost + currQueueItem.node.get_edge(action)[1]
				newAction = QueueItem(action, currQueueTuple, totalPathCost)
				newActionValue = calculateValue(newAction, method)
				newActionTuple = (newActionValue, newAction)
				queue.put_nowait(newActionTuple)
				queue = printQueueState(queue)
		if method == "beam":
			first = queue.get()
			second = queue.get()
			queue = PriorityQueue(maxsize=0)
			queue.put_nowait(first)
			queue.put_nowait(second)
		if method == "hill climbing":
			first = queue.get()
			queue = PriorityQueue(maxsize=0)
			queue.put_nowait(first)
	return "fail"

