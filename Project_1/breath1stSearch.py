graph = {'S': set(['A', 'D']),
         'A': set(['B', 'D']),
         'B': set(['C', 'EOFError']),
         'D': set(['E']),
         'F': set(['E']),
         'G': set(['F'])}
def breath1stSearch(nodeList, start, goal):
	queue = [(start, [start])]
	while queue:
		(node, path) = queue.pop(0)
		for next in nodeList(node) - set(path):
			print(path)
			if next == goal:
				yield path + [next]
			else:
				queue.append((next, path + [next]))
list(breath1stSearch(graph, 'S','G'))