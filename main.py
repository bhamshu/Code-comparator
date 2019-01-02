#make a function comparator too
#be smart in testcase generation. check edgecases, random etc.
#should handle tle too

def main():
	import os

	projectdirpath = input("Enter project directory or simply press Enter if it's in current directory: ") or '.'
	
	projectdir = os.listdir(projectdirpath) 
	files = [f for f in projectdir if os.path.isfile(f) if f[:4]=="code"]
	if len(files)>=2:
		print(f"Detected {len(files)} files {files} to compare. Great!")

	else:
		f0 = input("Enter the path of the first code file: ") 
		f1 = input("Enter the path of the second code file: ")
		files = [f0, f1]
	if "mycases.txt" in projectdir:
		print("Using the 'mycases.txt' as testcases. If you don't want that, remove it and rerun this script.")
		ipfile = None

	elif "thein.txt" in projectdir:
		ipfile = input("Detected 'thein.txt'. Please make sure that it is the correct input-format file and press Enter. Alternatively, type the path to input-format file: ") or projectdirpath+"/"+"thein.txt"

	else:
		from template import buildtemplate
		buildtemplate(projectdirpath)
		ipfile = input("Kindly edit the newly generated 'thein.txt' in your project directory and press Enter here or input the location of input format file: ") or projectdirpath+"/"+"thein.txt"

	testcases = projectdirpath+"/mycases.txt"
	# if testcases[0]==testcases[-1]=='"':
	# 	testcases=testcases[1:-1]
	condn = None#condn =  input("Enter constraints(if any) imposed on the testcases: ")

	if ipfile!=None:
		testcases = projectdirpath+"/thecases.txt"
		if ipfile[0]==ipfile[-1]=='"':
			ipfile=ipfile[1:-1]
		from testcase_generator import driver 
		driver(ipfile, testcases, condn)
	
	for thefile in files:
		lang = thefile[::-1][:thefile[::-1].index(".")][::-1]
		print(thefile)
			
		if lang == "cpp" or lang == "c":
			com = None
			if lang=="cpp":
				com = "g++"
			elif lang == "c":
				com = "gcc"
			#don't skip deleting! it won't work correctly else. if the compiling is taking too much time, make ad hoc edits
			delet ="	&&del temporaryexecutable.exe"

			built = f"{com} -o temporaryexecutable {thefile} && "
			if "temporaryexecutable.exe" in os.listdir(projectdirpath):
				built = ""
			os.system(built+f"temporaryexecutable <{testcases}> \"out{thefile[:-len(lang)]}txt\" "+delet)
		elif lang == "py":
			com = "py"
			print(f"{com} \"{thefile}\" <\"{testcases}\"> \"out{thefile[:-len(lang)]}txt\"")
			os.system(f"{com} \"{thefile}\" <\"{testcases}\"> \"out{thefile[:-len(lang)]}txt\"")
		elif lang == "java":
			com = "javac"
			#print(f"{com} {thefile} & java {thefile[:-len(lang)-1]} <{testcases}> out{thefile[:-len(lang)]}txt")
			os.system(f"{com} \"{thefile}\" & java \"{thefile[:-len(lang)-1]}\" <\"{testcases}\"> \"out{thefile[:-len(lang)]}txt\" ")
			def deleteclassfiles():
				# print(projectdir, projectdir[3][-5:])
				# cfil = [f for f in projectdir if os.path.isfile(f) if f[-5:]=="class"]
				# print(cfil)
				# for i in cfil:
					# os.system(f"del {i}")
				os.system(f"del \"{thefile[:-len(lang)]}class\" & del \"{thefile[:-len(lang)-1]}$FastReader.class\"")
			deleteclassfiles()

	from comparator import compare
	theoutfiles = ["out"+thefile[:-len(  thefile[::-1][:thefile[::-1].index(".")][::-1]  )]+"txt" for thefile in files]
	if "outcode.txt" in os.listdir(projectdirpath):
		ds = compare(projectdirpath, theoutfiles, sol = "outcode.txt")
		for l in range(len(ds)):
			if theoutfiles[l]=="outcode.txt":
				continue
			nd, ls, eqlen = ds[l]
			print("")
			if nd == 0:
				print(f"Congrats, {theoutfiles[l]} matches with outcode.txt. However, that doesn't necessarily means that the codes will always produce same output for same input. Run again for more confidence.")
			else:
				print(f"Points of difference between {theoutfiles[l]} and outcode.txt found in statements {[i+1 for i in ls]}.")
			print(f"Total number of differences = {len(ls)}")
			if not eqlen:
				print("Note that the two files do not have same number of lines.")
	else:
		nd, ls, eqlen = compare(projectdirpath, theoutfiles)[0]
		if nd == 0:
			print("Congrats, all the files match. However, that doesn't necessarily means that the codes will always produce same output for same input. Run again for more confidence.")
		else:
			print(f"Points of difference found in statements {[i+1 for i in ls]}.")
		if not eqlen:
			print("Not all output files have same number of lines.")

if __name__=="__main__":
	main()