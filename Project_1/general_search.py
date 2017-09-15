
def general_search(problem, method):
	q = make_queue(node, method)
	opened_nodes = list()
	visited = set()
	while(q):
		node = q.pop()
		visited.add(node)
		if(goal_test(node)):
			return 'pass'
		opened_nodes=expand(node)
		queue_sort(opened_nodes, method)
	return 'fail'


