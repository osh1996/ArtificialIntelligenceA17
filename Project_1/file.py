f = open("graph.txt", "r")
l = list()
q = list()
for line in f:
	l.append(line)
for item in l:
	q.append(item.split())
print q