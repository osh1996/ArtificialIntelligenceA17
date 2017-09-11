import Queue

class GeneralSearch:
	
	def generalSearch(self, startNode, method, queueType):
		startNodeName = "S"
		goalNodeName = "G"

		queue = queueType
		queue.put_nowait(startNode)
		visited = set()

		while(queue):
			node = queue.pop()
			if node.name == goalNodeName:
				return node
			visited.add(node)
			openedNodes = node.expand()
			for move in openedNodes:
				queue.put_nowait(move)
		return "fail"

	def expand(self, node):
		possibleMoves = set()
		for edge in node.edges:
			adjacentNode = edge[0]
			possibleMoves.add(adjacentNode)
		return possibleMoves
