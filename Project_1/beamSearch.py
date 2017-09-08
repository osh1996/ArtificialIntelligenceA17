def beamSearch(nodeList, start, goal):
	queue = list[list[start]]
	path = list[]
	print("Beam Search (w=2)")
	while queue:
		parent = findMin(queue)
		queue.remove(parent)
		parentName = removeCost(parent)
		path.append(parent[1],parentName)
		print(path)
		if parentName == goal:
			print(path)
			return 
		else:
			children = list[]
			children = getNeigh(parent)
			for item in children:
				queue.append(edges(1),edges(0),parentName)
			#checks if the queue is larger than w, and removes the highest cost paths until it is the size of w
			while len(queue)>2:
				remove(findMax(queue))
				
				
#removes the cost from the edge
def removeCost(edges)
	noCostList = list[]
	for item in edges:
		noCostlist.append(edges[0])
	return noCostList

#finds the path with the highest cost
def findMax(listoflists)
	max = 0;
	for item in listoflists
		if item[0] > max:
			item[0] = max
	return max

#finds path with the lowest cost
def findMin(listoflists)
	min = 0;
	for item in listoflists
		if item[0] > min:
			item[0] = min
	return min