from queue import PriorityQueue

def uniformCostSearch(nodeList, start, goal)
	visited = set()
	queue = PriorityQueue()
	queue.put((0,start))
	while queue:
		cost, node = queue.get()
			if node not in visited:
				visited.add(node)
				if node == goal:
					return
				