def calculateValue(path, moethod):
	output = -1
	if(method == 'uniform_cost'):
		output = path.pathCost
	if(method == 'greedy'):
		output = path.node.heuristic
	if(mehtod == 'astar'):
		output = path.node.heuristic + path.pathCost
	if(method == 'hill_climbing'):
		output = path.node.heuristic
	if(method == 'beam'):
		output = path.node.heuristic
	if(method == 'depth_limited'):
		output = path.prevNode.fnValue - 1
	if(method == 'iterative_deepening'):
		output = path.prevNode.fnValue - 1

	path.fnValue = output
	return output
