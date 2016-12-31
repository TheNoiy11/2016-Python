def MaxMin(list):
	if len(list) == 0:
		print("GOT THERE")
		return (0, 0)
	(max, min) = MaxMin(list[1:])
	if list[0] > max:
		return (list[0], min)
	elif list[0] < min:
		return (max, list[0])
	return (max,min)
	
print(MaxMin([-1,2,1000000000000,-100,3,-2]))