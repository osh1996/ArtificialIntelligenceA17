def breath1stSearch(nodeList, start, goal):
	queue = [(start, [start])]
	while queue:
		(node, path) = queue.pop(0)
		for next in nodeList(node) - set(path):
			print(path)
			if next == goal:
				return path + [next]
			else:
				queue.append((next, path + [next]))
print "Breath First Search"