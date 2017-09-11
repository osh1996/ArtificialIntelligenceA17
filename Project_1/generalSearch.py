import Queue
import queueItem
from node import Node


def generalSearch(self, method, initQueue):
	goalNodeName = "G"
	queue = initQueue
	visited = set()
	while(queue):
		currNode = queue.pop()
		if currNode.node.name == goalNodeName:
			return "G"
		openedNodes = self.expand(currNode)
		for action in openedNodes:
			totalPathCost = currNode.pathCost + currNode.get_edge(action)[1]
			newAction = queueItem(action, currNode, totalPathCost)
			newAction.value = calculateValue(newAction, method)
			queue.put_nowait(newAction)
			visited.add(newAction)
		return "fail"
		

	# returns a set of all outgoing edges from a given node
def expand(self, node):
	possibleMoves = set()
	for edge in node.edges:
		adjacentNode = edge[0]
		possibleMoves.add(adjacentNode)
	return possibleMoves

	# calculates f(n) for the given node in the search based on the algorithm used
def calculateValue(self, queueItem, searchMethod):
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
	return output

