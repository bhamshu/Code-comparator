def compare(thepath, args, sol = None):
	'''takes a directory and a list of files in it and finds points of differences'''
	f = [None]*len(args)
	for i in range(len(args)):
		theoutput = args[i]
		print(args[i])
		with open(thepath+"/"+theoutput) as l:
			f[i] = l.read().split("\n")

	if sol!=None:
		with open(thepath+"/"+sol) as l:
			thesol = l.read().split("\n")
		ds = []
		for i in f:
			if len(i) == len(thesol):
				eqlen = True
			else:
				eqlen = False

			l = min(len(i), len(thesol))
			nd = 0 #number of points of difference
			ls = []
			for j in range(l):
				if i[j]==thesol[j]:
					nd+=1
					ls.append(j)

			ds.append( (nd, ls, eqlen) )
		return ds

	else:
		lengths = [len(i) for i in f]
		if len(set(lengths)) == 1:
			eqlen = True
		else:
			eqlen = False

		l = min(lengths)
		nd = 0 #number of points of difference
		ls = []
		for j in range(l):
			g = [f[i][j] for i in range(len(args))]
			if len(set(g))!=1:
				nd+=1
				ls.append(j)

		return [(nd, ls, eqlen)]

def main():
	thepath = input("Enter the directory in which the files are located or press Enter if it's current directory: ") or "."
	ls = [input("Enter the names of the files one by one:\n")]
	while ls[-1]:
		ls.append(input())
	ls = ls[:-1]
	compare(thepath, ls)

if __name__ == '__main__':
	main()
