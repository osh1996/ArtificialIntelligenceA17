import Queue
import queueItem

class GeneralSearch:
	
	def generalSearch(self, currentNode, queue)
		goalNodeName = "G"

#		queue.put_nowait(startNode)
#		visited = set()

		if(queue):
			node = queue.pop()
			if node.name == goalNodeName:
				return "G"
			openedNodes = node.expand()
			for action in openedNodes:
				queue.put_nowait(move)
		

	def expand(self, node):
		possibleMoves = set()
		for edge in node.edges:
			adjacentNode = edge[0]
			possibleMoves.add(adjacentNode)
		return possibleMoves
