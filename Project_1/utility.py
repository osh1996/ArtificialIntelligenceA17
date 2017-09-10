def getNode(name, nodeObjects):
	for node in nodeObjects:
		if name == node.name:
			return node
	return -1