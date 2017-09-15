def expand(path, visited):
	out = list()
	edges = path.node.edges
	for item in edges:
		if(item[0].name not in visited):
			Path(item[0], path, path.pathCost + item[1])
	return out
