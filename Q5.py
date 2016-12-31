def three_answers(fulllist):
	if len(fulllist) == 0:
		return(0,0,0)
	elif fulllist[0] % 2 == 0:
		if fulllist[0] == 0:
			even,odd,zctr = three_answers(fulllist[1:])
			return (even, odd,zctr+1)
		else:
			even,odd,zctr = three_answers(fulllist[1:])
			return (fulllist[0]+even, odd,zctr)
	else:
		even,odd,zctr = three_answers(fulllist[1:])
		return (even, fulllist[0]+odd,zctr)

print(three_answers([0,3,3,2,0,1]))