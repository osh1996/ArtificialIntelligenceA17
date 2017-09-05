def breath1stSearch(nodeList, start, goal):
	queue = [(start, [start])]
	while queue:
		(node, path) = queue.pop(0)
		for next in nodeList(node) - set(path):
			if next == goal:
				yield path + [next]
			else:
				queue.append((next, path + [next]))
list(bfs_paths(graph, 'S', 'G'))
print "Breath First Search"