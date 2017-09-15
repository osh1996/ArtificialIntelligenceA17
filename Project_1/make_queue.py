from node import Node
import Queue

def make_queue(node,method):
	if(method == 'dfs'):
		q = Queue.LifoQueue(maxsize=0)
		q.add(node)
	if(method == 'bfs'):
		q = Queue.Queue(maxsize=0)
		q.add(node)
	if(method == 'depth_limited'):
		q = Queue.Queue(maxsize=0)
		q.add(node)
	if(method == 'iterative_deepening'):
		q = Queue.Queue(maxsize=0)
		q.add(node)
	if(method == 'uniform_cost'):
		q = Queue.PriorityQueue(maxsize=0)
		q.add(node)
	if(method == 'greedy'):
		q = Queue.PriorityQueue(maxsize=0)
		q.add(node)
	if(method == 'astar'):
		q = Queue.PriorityQueue(maxsize=0)
		q.add(node)
	if(method == 'hill_climbing'):
		q = Queue.PriorityQueue(maxsize=0)
		q.add(node)
	if(method == 'beam'):
		q = Queue.PriorityQueue(maxsize=0)
		q.add(node)