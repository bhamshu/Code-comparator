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
			delet = " " or "&&del temporaryexecutable.exe"
			built = f"{com} -o temporaryexecutable {thefile} && "
			if "temporaryexecutable.exe" in os.listdir(projectdirpath):
				built = ""
			os.system(built+f"temporaryexecutable <{testcases}> out{thefile[:-len(lang)]}txt"+delet)
		elif lang == "py":
			com = "py"
			os.system(f"{com} {thefile} <{testcases}> out{thefile[:-len(lang)]}txt")

	from comparator import compare
	compare(projectdirpath, ["out"+thefile[:-len(  thefile[::-1][:thefile[::-1].index(".")][::-1]  )]+"txt" for thefile in files])

if __name__=="__main__":
	main()
