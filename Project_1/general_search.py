
def general_search(startNode, method):
	q = make_queue(startNode, method)
	opened_nodes = list()
	visited = set()
	while(q):
		node = q.pop()
		visited.add(node)
		if(goal_test(node)):
			return 'pass'
		opened_nodes = expand(node)
		q = queue_sort(q, node, opened_nodes, method)
	return 'fail'

def queue_sort(queue, node, opened_nodes, method):
	q = queue
	for path in opened_nodes:
		q.put_nowait(path)