import Queue
q = Queue.LifoQueue(maxsize=0)

def dfs(start, q):
	q.put_nowait(start)
	if not any(get_Neigh(start)):
		edges = get_Neigh(start)
		q.put_nowait(start)
		dfs(q.get_nowait(), q)
	else:
		if(q.empty):
			return 0
		else:
			dfs(q.get_nowait(), q)


		




