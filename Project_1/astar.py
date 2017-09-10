from Queue import PriorityQueue

q = Queue.PriorityQueue(maxsize=0)
visited = set()
def astar(node, q, cost = 0, visited = None):
	visited.add(node)

	if(node is goal):
		return 1
	else:
		edges = node.edges
		for item in edges:
			priority = item[0].heuristic + item[1] + cost
			q.put((priority,item)) #places all edges in priorityqueue
		next_node = q.pop()
		astar(next_node[1], q, next_node[0], visited)