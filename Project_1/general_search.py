from Queue import PriorityQueue
from node import Node
import Queue

def general_search(start, method):
	q = make_queue(start, method)
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
	if method == "hill_climbing":
		first = q.get_nowait()
		q = PriorityQueue()
		q.put_nowait(first)
	if method == "beam":
		first = q.get_nowait()
		second = q.get_nowait()
		q = PriorityQueue()
		q.put_nowait(first)
		q.put_nowait(second)
	return q



def goal_test(node):
	if(node):
		if (node.name == 'G'):
			return True
		return False

def expand(path, visited):
	out = list()
	edges = path.node.edges
	for item in edges:
		if(item[0].name not in visited):
			Path(item[0], path, path.pathCost + item[1])
	return out


def make_queue(startNode,method):
	if(method == 'dfs'):
		q = Queue.LifoQueue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'bfs'):
		q = Queue.Queue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'depth_limited'):
		q = Queue.Queue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'iterative_deepening'):
		q = Queue.Queue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'uniform_cost'):
		q = Queue.PriorityQueue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'greedy'):
		q = Queue.PriorityQueue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'astar'):
		q = Queue.PriorityQueue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'hill_climbing'):
		q = Queue.PriorityQueue(maxsize=0)
		q.put_nowait(startNode)
	if(method == 'beam'):
		q = Queue.PriorityQueue(maxsize=0)
		q.put_nowait(startNode)
		

