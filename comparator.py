def compare(thepath,args):
	'''takes a directory and a list of files in it and finds points of differences'''
	f = [None]*len(args)
	for i in range(len(args)):
		theoutput = args[i]
		print(args[i])
		with open(thepath+"/"+theoutput) as l:
			f[i] = l.read().split("\n")

	lengths = [len(i) for i in f]
	if len(set(lengths)) == 1:
		print("Good News, the output files all have equal number of files. At least. Phew!")
	else:
		print("Well, not all putput files have same number of lines. Please open the text files and see.")

	l = min(lengths)
	nd = 0 #number of points of difference
	for j in range(l):
		if nd>3:
			print("At least three points of difference have been reported. First address those please. ")
			break
		g = [f[i][j] for i in range(len(args))]
		if len(set(g))!=1:
			nd+=1
			print(f"A point of difference found in sentence {j+1}.")
			
