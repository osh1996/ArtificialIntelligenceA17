graph = {'S': set(['A', 'D']),
         'A': set(['B', 'D']),
         'B': set(['C', 'E']),
         'D': set(['E']),
         'F': set(['E']),
         'G': set(['F'])}
def breath1stSearch(nodeList, start, goal):
	queue = [(start)]
	path = set([])
	print("Breath First Search")
	while queue:
		node = queue.pop(0)
		path.add(sorted(getNeigh(node)))
		for edge in set[path]:
			print(path)
			if next == goal:
				path.add(next)
				print(path)
			else:
				queue.append((next, path + [next]))
				queue.sort()

