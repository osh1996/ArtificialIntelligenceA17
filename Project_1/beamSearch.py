def beamSearch(nodeList, start, goal)
	print("Beam Search (w=2)"):
	totalcost = int()
	queue = list[start]
	while queue:
		parent = findMin(queue)
		queue.remove(parent)
		if parent == goal:
			return 
		else:
			children = list[]
			children = parent.edges
			for item in children:
				totalcost = parent(0) +item[2]
				queue.append(item)
			#checks if the queue is larger than 
			#w, and removes the highest cost paths until it is the size of w
			while len(queue)>2:
				remove(findMax(queue))
				

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