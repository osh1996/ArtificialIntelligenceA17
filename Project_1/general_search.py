def general_search(problem, method):
	q = make_queue(node, method)
	while(flag):
		if(q.empty()):
			return 'fail'
		node = q.pop()
		if(goaltest(node)):
			return 'pass'
		opened_nodes=expand(node)
		queue_sort(opened_nodes, method)



