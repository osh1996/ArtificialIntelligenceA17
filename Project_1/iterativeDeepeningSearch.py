def iterativeDeepeningSearch(node):
	i = 0
	for i in to_infinity():
		depthLimitedSearch(node, i)




def to_infinity():
    index=0
    while 1:
        yield index
        index += 1
