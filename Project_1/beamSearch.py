def beamSearch(nodeList, start, goal):
	queue = [ "start"]
	while queue:
		if queue.pop(0) == goal:
			yield path + queue.pop()
		else:
			children = queue.pop(0).nextnode
			#Need to work on how nodelists actually work
			queue.append(children)
			if len(queue)>2:
				queue.pop()