def expand(node, visited):
	out = list()
	edges = node.edges
	for item in edges:
		if(item[0].name not in visited):
			out.append(append)
	return out