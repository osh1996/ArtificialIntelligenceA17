from Queue import PriorityQueue
from node import Node
import Queue
from path import Path

def general_search(start, method):
	q = make_queue(start, method)
	opened_nodes = list()
	visited = set()
	while(q):
		if q.empty():
			return "fail"
		pathTuple = q.get_nowait()
		visited.add(pathTuple[1].node.name)
		if(goal_test(pathTuple[1].node)):
			return 'pass'
		opened_nodes = expand(pathTuple[1], visited, method)
		q = queue_sort(q, pathTuple, opened_nodes, method)
		if q is "fail":
			return "fail"
	return 'fail'

def queue_sort(queue, pathTuple, opened_nodes, method):
	q = queue
	if method != "depth_limited" or pathTuple[0] != 0:
		for path in opened_nodes:
			value = calculateValue(path, method)
			path.fnValue = value
			pathTuple = (value, path)
			print(path.node.name + " - " + str(path.fnValue))
			q.put_nowait(pathTuple)
	if method == "hill_climbing":
		print("hill-climbing")
		if not q.empty():
			first = q.get_nowait()
			q = PriorityQueue()
			q.put_nowait(first)
	if method == "beam":
		first = False
		second = False
		if not q.empty():
			first = q.get_nowait()
		if not q.empty():
			second = q.get_nowait()
		q = PriorityQueue()
		if first != False:
			q.put_nowait(first)
		if second != False:
			q.put_nowait(second)
	return q

def goal_test(node):
	if(node):
		if (node.name == 'G'):
			return True
		return False

def expand(path, visited, method):
	out = list()
	edges = path.node.edges
	for item in edges:
		if(item[0].name not in visited):
			p = Path(item[0], path, path.pathCost + item[1])
			out.append(p)
	return out

def calculateValue(path, method):
	output = -1
	if(method == 'uniform_cost'):
		output = path.pathCost
	if(method == 'greedy'):
		output = path.node.heuristic
	if(method == 'astar'):
		output = path.node.heuristic + path.pathCost
	if(method == 'hill_climbing'):
		output = path.node.heuristic
	if(method == 'beam'):
		output = path.node.heuristic
	if(method == 'depth_limited'):
		output = path.prevNode.fnValue - 1
	if(method == 'iterative_deepening'):
		output = path.prevNode.fnValue - 1

	return output


def make_queue(startNode,method):
	q = None
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
	return q
		

