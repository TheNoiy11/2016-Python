def THING(str,cut):
	newString = ""
	i = str.find(cut)
	if i == -1:
		return str
	else:
		newString = str[:i] + str[i + len(cut):]
	return newString		
print(THING("the bird bird bird the","bird"))