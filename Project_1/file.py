from node import node

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
		print ("added " + line + " to nodeList")

	else:
		
		edgeList.append(line)
		print ("added " + line + " to edgeList")

nodeList.remove('########\n')

#print (nodeList)
#print (edgeList)
nodeObjects = set()
for item in nodeList:
	current = item.split()
	name = current[0]
	heur = current[1]
	newNode = node(name, heur)
	nodeObjects.add(newNode)
	print (newNode)


	#current[0] = node(current[1])

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
