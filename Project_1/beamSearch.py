def beamSearch(nodeList, start, goal):
	queue = list[list[start]]
	print("Beam Search (w=2)")
	while queue:
		print(queue)
		parent = findMin(queue)
		queue.remove(parent)
		if parentName == goal:
			print(parent)
			return 
		parentName = removeCost(parent)
		else:
			children = list[]
			children = getNeigh(parent)
			for item in children:
				queue.append(item(1),item(0),parentName)
				print(queue)
			#checks if the queue is larger than 
			w, and removes the highest cost paths until it is the size of w
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