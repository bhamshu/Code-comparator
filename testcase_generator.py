#yet to handle conditions
def prereq():
	pass

from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters
lwr = lower = ascii_lowercase; upr = upper = ascii_uppercase; ltrs = letters = ascii_letters
import random
alphanum = letters+digits

def tcgen(statements, theoutput, condn=None):
	f = open(theoutput, "w")
	#print(statements)
	for statement in statements:
		main(statement, condn, f)
	f.close()


def main(statement, condn, f):
	if (statement == "" or statement[0]=="#"):
		return
	commented = False
	if statement[0] == statement[-1]==":":
		commented = True
		statement = statement[1:-1]

	if statement=="\\n":
		f.write("\n")
		return
	if statement[:8]!="nested$$":
		thestatement = statement.split("$$")#()
	else:
		statement = statement[8:]
		pt = statement.index("{")
		thestatement = [statement[:pt], statement[pt:]]
	#nested statement should be of the form>>>nested$$(10, "a"){st1;st2;st3}
	#last statement must not precede a semicolon.
	thecase, theend = eval(thestatement[0])
	if commented:
		thecase = 1
		if "{" in thestatement:
			raise BaseException("Nesting not allowed in commented statements.")

	for case in range(thecase):	
		if thestatement[1][0]=="{" and thestatement[1][-1]=="}":
			rstatements = thestatement[1][1:-1].split(";")
			#statements = statements.replace(" ","") //no ntead already done
			#statements = statements.split("\n") //split by ; here
			if "end" in rstatements:
				raise BaseException("end not allowed in nested statements")
			for rstatement in rstatements:
					main(rstatement, condn, f)
			f.write(theend)
			continue


		thetype = thestatement[1]
		thevar = thestatement[2]
		thedomain = thestatement[3]
		if thetype=="string":
			thedomain = eval(thedomain)
			# print(thedomain, type(thedomain[0]), type(thedomain[1]))
			thelength = thedomain[1]
			thedomain = thedomain[0]
			if type(thedomain)==set:
				thedomain = tuple(thedomain)
			theval = ''.join(random.choices(thedomain, k=thelength))

		else:
			thedomain = eval(thedomain)
			if type(thedomain)!=int:
				thedomain = set(thedomain)
			else:
				thedomain = set([thedomain])
			#thedomain = map(thetype, thedomain) needed?
			theval = random.choice(tuple(thedomain))
		#if thedomain is in the form of a range, we can find out the edge cases by min, max. If it's random.something,
		#we need to look at the arguments before evaluating the expression. Do all that here
		#take explicit edge cases, special cases from the user too
		if type(theval)==str:
			exec(thevar+f"='{theval}'", globals())
		else:
			exec(thevar+f"={theval}", globals())
		
		if commented:
			continue #don't write it to file

		f.write(str(theval)) #use random.sample when you are making it smart and efficient.
		f.write(theend)

def driver(ipfile, condn, testcases):
	prereq()
	with open(ipfile) as ip:
		statements = ip.read()
	statements = statements.replace(" ","")
	statements = statements.split("\n")
	if "end" in statements:
		statements = statements[:statements.index("end")]
	#only 10 macros (macro0, ..., macro9) are allowed.
	MACRO = {}
	for j in range(len(statements)-1, -1, -1):
		#statement = statements[j]
		for k, v in MACRO.items():
			if k in statements[j]:
				#print(k, v, statements[j])
				statements[j] = statements[j].replace(k, v)

		if statements[j][:5].upper() == "MACRO":
			MACRO[statements[j][:6]] = statements[j][8:]
			del statements[j]
			continue
	#print(statements)
	tcgen(statements, testcases, condn)


if __name__=="__main__":
	ipfile = input("Enter the absolute location of input format file: ")
	if ipfile[0]==ipfile[-1]=='"':
		ipfile=ipfile[1:-1]
	condn = None#condn =  input("Enter constraints(if any) imposed on the testcases: ")
	
	testcases = input("Enter the location of the testcases file to be built: ")
	if testcases[0]==testcases[-1]=='"':
		testcases=testcases[1:-1]
	driver(ipfile, condn, testcases)


# This code has been found to work correctly on the following cases:

#this one won't work because comments changed, string range changed
# (1, "")$$int$$a$$range(10, 15)
# \n
# :b = 10:
# (a, "\n")$$string$$c$$lwr+upper, b

# (1, "")$$int$$a$$range(10, 15)
# \n
# (a, "\n")$$string$$c$$lwr+upper, random.randint(1, 10)

# (1, "")$$int$$a$$range(10, 15)
# \n
# :(1, "")$$int$$b$$10:
# (a, "\n")$$string$$c$$(lwr+upper, random.randint(1, b))

#(1, "")$$int$$a$$range(10, 15)
#\n
#:(1, "")$$int$$b$$10:
#(a, "\n")$$string$$c$$({"a", "b"}, random.randint(1, b))
#nested$$(10, "a\n"){(1, "ADS")$$char$$f$$digits}

# 1, "\n")$$int$$t$$range(1, 10**2)
# nested$$(t, ""){(1, "\n")$$int$$l$$range(1, 10**4); (1, "\n")$$string$$s$$(lwr, l)}

# (1, "\n")$$int$$t$$range(1, 10**2)
# nested$$(t, "")MACRO0
# MACRO0$${(1, "\n")$$int$$l$$MACRO1(1, "\n")$$string$$s$$(lwr, l)}
# MACRO1$$range(1, 10**4);


# the single hashes are context, the double hashes consists of actually archived code.
	# if (statement == "" or statement[0]=="#"):
	# 	return
	# #towrite = ""; if writing many times is a concern, use this. be careful when implementing recursion.
	
	# #the following block was when comments were of type :b=3:. Now they are like regular statements
	# # if statement[0] == statement[-1]==":":
	# # 	statement = statement[1:-1]
	# # 	if set(statement).issubset(set(alphanum).union({'=', '+', '-', '*', '/', 'e'})):
	# # 		exec(statement, globals())
	# # 	else:
	# # 		print(f"There's something wrong with one of your comment statements {statement}")
	# # 		assert 1==0
	# # 	return	
	# commented = False
	# if statement[0] == statement[-1]==":":
	# 	commented = True
	# 	statement = statement[1:-1]