from Queue import PriorityQueue

def general_search(startNode, method):
	q = make_queue(startNode, method)
	opened_nodes = list()
	visited = set()
	while(q):
		node = q.get_nowait()
		visited.add(node)
		if(goal_test(node)):
			return 'pass'
		opened_nodes = expand(node)
		q = queue_sort(q, node, opened_nodes, method)
	return 'fail'

def queue_sort(queue, node, opened_nodes, method):
	q = queue
	if method != "depth limited" or currQueueTuple[0] != 0:
		for path in opened_nodes:
			q.put_nowait(path)
	if method == "hill climbing":
		first = q.get_nowait()
		q = PriorityQueue()
		q.put_nowait(first)
	if method == "beam"