from Queue import PriorityQueue

q = PriorityQueue(maxsize=0)
visited = set()
def astar(node, q, cost = 0, visited = None):
	
	visited.add(node) #add node to visited set

	if(node is goal): #goal test
		return True
	
	else:
		edges = list(node.edges)
		for item in edges:
			priority = item[0].heuristic + item[1] + cost #adds the heuristic of the item +  path weight + total cost so far
			q.put((priority,item)) #places all edges in priorityqueue prioritized by lowest f(n)

		if q.empty(): # if q empty failed
			return False
		
		next_node = q.pop() # gets lowest cost q
		astar(next_node[1], q, next_node[0], visited) #recurse on next node using cost = priority of that node