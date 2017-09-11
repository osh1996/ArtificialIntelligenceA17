def breath1stSearch(nodeList, start, goal):
	queue = [(start)]
	path = set([])
	print("Breath First Search")
	while queue:
		node = queue.pop(0)
		path.add(node[1])
		print(path)
		path.add(sorted(getNeigh(node)))
		for edge in set[path]:
			print(path)
			if next == goal:
				path.add(next)
			else:
				queue.append((next, path + [next]))
				queue.sort()

