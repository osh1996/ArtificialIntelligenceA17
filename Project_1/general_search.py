from Queue import PriorityQueue
from node import Node
import Queue

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

def goal_test(node):
	if(node):
		if (node.name = 'G'):
			return True
		return False

def expand(path, visited):
	out = list()
	edges = path.node.edges
	for item in edges:
		if(item[0].name not in visited):
			Path(item[0], path, path.pathCost + item[1])
	return out


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