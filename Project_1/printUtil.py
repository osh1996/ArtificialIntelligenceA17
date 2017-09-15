def printLabels(method):
	outputFile = open("output.txt", 'a')

	if method is "bfs":
		outputFile.write("\nBreadth First Search\n")
	if method is "dfs":
		outputFile.write("\nDepth First Search\n")
	if method is "depth_limited":
		outputFile.write("\nDepth-limited Search (limit = 2)\n")
	if method is "uniform_cost":
		outputFile.write("\nUniform Cost Search\n")
	if method is "greedy":
		outputFile.write("\nGreedy Search\n")
	if method is "astar":
		outputFile.write("\nA* Search\n")
	if method is "hill_climbing":
		outputFile.write("\nHill Climbing\n")
	if method is "beam":
		outputFile.write("\nBeam Search (w=2)\n")


	outputFile.write("\tExpanded\t\tQueue\n\t\t")
	outputFile.close()

def printLabelsIDS(depth):
	file = open("output.txt", 'a')
	if depth is 0:
		file.write("\nIterative Deepening Search\n")
	output = "\n\tExpanded\t\tQueue\nL="+str(int(depth))+"\t\t"
	file.write(output)
	file.close()

def printLine(queue, method):
	file = open("output.txt", 'a')
	queueList = list(queue.queue)
	print(queueList)
	first = True
	for pathTuple in queueList:
		name = pathTuple[1].node.name
		if first is True:
			file.write(name+"\t\t[")
			first = False
		if pathTuple[0] is not -1:
			if method is not "depth_limited" and method is not "iterative_deepening":
				file.write(str(pathTuple[0]))
		file.write("<"+name)
		path = pathTuple[1].prevNode
		while path is not None:
			file.write(","+path.node.name)
			path = path.prevNode
		file.write("> ")

	file.write(" ]\n\t\t")
	file.close()

def printResult(result):
	file = open("output.txt", 'a')
	if result is "pass":
		file.write("goal reached!\n\n")
	else:
		file.write("\n")
	file.close()