from queueItem import QueueItem
from utility import printQueueState
from node import Node

	# returns a set of all outgoing edges from a given node
def expand(node):
	possibleMoves = set()
	for edge in node.edges:
		adjacentNode = edge[0]
		possibleMoves.add(adjacentNode)
	return possibleMoves

	# calculates f(n) for the given node in the search based on the algorithm used
def calculateValue(queueItem, searchMethod):
	output = "uninformed"
	if searchMethod == "depth limited":
		output = (queueItem.prevNode.value) - 1
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
	visited = set()
	while(queue):
		currQueueTuple = queue.get_nowait()
		currQueueItem = currQueueTuple[1]
		print(currQueueItem.node.name)
		if currQueueItem.node.name == goalNodeName:
			return "G"
		openedNodes = expand(currQueueItem.node)
		for action in openedNodes:
			if method != "depth limited" or currNode.value != 0:
				totalPathCost = currQueueItem.pathCost + currQueueItem.node.get_edge(action)[1]
				newAction = QueueItem(action, currQueueItem, totalPathCost)
				newActionTuple = (calculateValue(newAction, method), newAction)
				print(newAction.node.name)
				queue.put_nowait(newActionTuple)
				visited.add(newActionTuple)
				print
				queue = printQueueState(queue)
		if method == "beam":
			first = queue.get_nowait()
			second = queue.get_nowait()
			queue = PriorityQueue(maxsize=0)
			queue.put_nowait(first)
			queue.put_nowait(second)
		if method == "hill climbing":
			first = queue.get_nowait()
			queue = PriorityQueue(maxsize=0)
			queue.put_nowait(first)
	return "fail"

