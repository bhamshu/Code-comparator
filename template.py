def buildtemplate(thepath = ".", mode = "noob"):
	f = open(thepath +"/"+"thein.txt", "w")
	if mode == "noob":
		f.write("#Scroll to the end of the file if you don't know what this means.\n")

	from string import ascii_lowercase as lwr
	for i in lwr:
		f.write(f'(1, "")$$int$${i}$$range(10, 15)\n')

	if mode == "noob":
		f.write('''#this self referential statement might as well not exist because it starts with a hash symbol
		#this is a comment>>> :(1, "")$$int$$pi$$3.14:	>>>because it is flanked by colons. This will be evaluated (for further use, maybe) but not f.writeed
		#this is a normal statement>>> (a, "\\n")$$	char$$c$$lwr
		end
			No further statements will be encountered if a statement consists of only "end". 
			This isn't even being read by the code.
		(first, second) at the start of a statement means the statement is to be repeated -first- number of times and the -second- is to be f.writeed after each repetition
		Next comes type. Then comes variable name. Then comes the set of values it can assume
		nested statement should be of the form>>>nested$$(10, "a"){st1;st2;st3}
		last statement in a nested set of statements must not precede a semicolon.'''.replace("\t", ""))

		f.write('''#Try the following statements normally (before end) if you wish:
			(1, "ADS")$$char$$f$$digits
			(1, "")$$int$$a$$range(10, 15)
			(a, "\\n")$$string$$c$$({"a", "b"}, random.randint(1, b))
			(0, "whatever it won't be f.writeed")$$int$$lol$$10
			the above statement with 1 instead of 0 in the start
			>>> \\n
			simply will f.write an endline
			The following is the way to execute scripts in your input format. Greatly simplifies the things. Simply "print" what you want to be written in your testcases file.
			script$$
			import random

			c=''.join(random.sample(lwr, 26))
			b = random.randint(1, MACRO1)
			print(b)
			print(c)
			for j in range(b-1):
				s = ''.join(random.sample(lwr, random.randint(1,26)))
				print(s, end=" ")
			s = ''.join(random.sample(lwr, random.randint(1,26)))
			print(s)

			$$script
			MACRO1$$10
			'''.replace("\t", ""))
	f.close()

if __name__=="__main__":
	buildtemplate()