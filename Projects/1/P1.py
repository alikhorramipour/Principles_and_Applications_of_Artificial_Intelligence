open = []	#list of open nodes
closed = [] #list of checked nodes

while not open:
	minF = 999999
	nodeWithMinF = null
	for node in open:
		if node.f > minF:
			nodeWithMinF = node
			minF = nodeWithMinF.f
	open.remove(nodeMinF)
