def symmetric(inputlist):
	if inputlist==[]:
		return True
	if len(inputlist)!=len(inputlist[0]):
		return False
	size=len(inputlist)
	horizontalindex=0
	while horizontalindex<=size-1:
		verticalindex=0
		while verticalindex<=size-1:
			if inputlist[verticalindex][horizontalindex]==inputlist[horizontalindex][verticalindex]:
				verticalindex=verticalindex+1
			else:
				return False
		horizontalindex=horizontalindex+1
	return True