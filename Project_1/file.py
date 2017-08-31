f = open("graph.txt", "r")
l = list()
q = list()
for line in f:
	l.append(line)
for item in l:
	q.append(item.split())
print q

#Depth 1st Search
#Breath 1st Search
#Depth-limited Search Depth-limit-2
#Iterative Deepening Search showing all iterations
#Uniform Cost Search
#Greedy Search
#A*
#Hill-climbing
#Beam Search W=2
