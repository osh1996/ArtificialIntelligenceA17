import Node

f = open("graph.txt", "r")
nodeList = list()
edgeList = list()

q = list()
flag = 0
for line in f:
	if "#" in line:
		flag = 1

	if flag == 1:
		nodeList.append(line)
		print "added " + line + " to nodeList"

	else:
		edgeList.append(line)
		print "added " + line + " to edgeList"




#for item in l:
#	q.append(item.split())
#print q

#Depth 1st Search
#Chris
#Breath 1st Search
#Tung
#Depth-limited Search Depth-limit-2
#David
#Iterative Deepening Search showing all iterations
#Chris
#Uniform Cost Search
#Tung
#Greedy Search
#David
#A*
#Chris
#Hill-climbing
#David
#Beam Search W=2
#Tung
