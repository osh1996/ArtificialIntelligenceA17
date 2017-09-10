from queue import PriorityQueue

def uniformCostSearch(nodeList, start, goal)
	visited = set()
	queue = PriorityQueue()
	queue.put((start.heuristic,start))
	while queue:
		cost, node = queue.get()
			if node not in visited:
				visited.add(node)
				if node == goal:
					finalPath.append[total_cost, visited]
					return finalPath
				for i in graph.neighbors(node):
					if i not in visited:
						total_cost = cost + graph.get_cost(node, i)
						queue.put((total_cost, i))
					