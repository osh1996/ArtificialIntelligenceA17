def printLabels():
	file = open("output.txt", 'a')
	output = "\tExpanded\t\tQueue\n\t\t"
	file.write(output)
	file.close()

def printLabelsIDS(depth):
	file = open("output.txt", 'a')
	output = "\tExpanded\t\tQueue\nL="+str(int(depth))+"\t"
	file.write(output)
	file.close()