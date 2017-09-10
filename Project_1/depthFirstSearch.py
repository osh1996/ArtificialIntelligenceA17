from Queue import LifoQueue

q = LifoQueue(maxsize=0)

def dfs(node, q, goal):
	
	if (node is goal): #goal test
		return True
	
	q.put_nowait(node) #placing first node in q
	
	if not any(node.edges):	# if not a leaf
		edges = list(node.edges) 
		for item in edges: 
			q.put(item[0]) #place object of edge in q
		dfs(q.get_nowait(), q) # recurse on q pop
	
	else: # leaf
		if(q.empty()): #empty q = done
			return True
		else:
			dfs(q.get_nowait(), q) # recurse on q pop


		




