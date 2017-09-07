def beamSearch(nodeList, start, goal):
	queue = list()
	queue.append(start)
	path = list()
	print("Beam Search (w=2)")
	while queue:
		firstnode = queue.pop(0)
		if firstnode == goal:
			return path + queue.pop()
		else:
			children = list()
			firstnode.edges
			queue.append(children)
			return
			#checks if the queue is larger than w, and removes the highest cost paths until it is the size of w
			while len(queue)>2:
				
def removeCost(edges)
	noCostList = list()
	for item in edges:
		noCostlist.append(edges[0])
	return noCostList()