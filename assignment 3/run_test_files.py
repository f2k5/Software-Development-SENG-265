import subprocess
import sys
from termcolor import colored, cprint

print("===============================")
print("======== TESTING FILES ========")
print("===============================")

#Test case: 1
subprocess.call("python sengfmt2.py in01.txt > 1.txt", shell=True)
if subprocess.call(["diff", "-b", "1.txt", "out01.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 1,  in01.txt -> PASSED", "white"))
else:
	print(colored("Test case 1,  in01.txt -> FAILED", "red"))

#Test case: 2
subprocess.call("python sengfmt2.py in02.txt > 2.txt", shell=True)
if subprocess.call(["diff", "-b", "2.txt", "out02.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 2,  in02.txt -> PASSED", "white"))
else:
	print(colored("Test case 2,  in02.txt -> FAILED", "red"))

#Test case: 3
subprocess.call("python sengfmt2.py in03.txt > 3.txt", shell=True)
if subprocess.call(["diff", "-b", "3.txt", "out03.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 3,  in03.txt -> PASSED", "white"))
else:
	print(colored("Test case 3,  in03.txt -> FAILED", "red"))

#Test case: 4
subprocess.call("python sengfmt2.py in04.txt > 4.txt", shell=True)
if subprocess.call(["diff", "-b", "4.txt", "out04.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 4,  in04.txt -> PASSED", "white"))
else:
	print(colored("Test case 4,  in04.txt -> FAILED", "red"))

#Test case: 5
subprocess.call("python sengfmt2.py in05.txt > 5.txt", shell=True)
if subprocess.call(["diff", "-b", "5.txt", "out05.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 5,  in05.txt -> PASSED", "white"))
else:
	print(colored("Test case 5,  in05.txt -> FAILED", "red"))

#Test case: 6
subprocess.call("python sengfmt2.py in06.txt > 6.txt", shell=True)
if subprocess.call(["diff", "-b", "6.txt", "out06.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 6,  in06.txt -> PASSED", "white"))
else:
	print(colored("Test case 6,  in06.txt -> FAILED", "red"))

#Test case: 7
subprocess.call("python sengfmt2.py in07.txt > 7.txt", shell=True)
if subprocess.call(["diff", "-b", "7.txt", "out07.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 7,  in07.txt -> PASSED", "white"))
else:
	print(colored("Test case 7,  in07.txt -> FAILED", "red"))

#Test case: 8
subprocess.call("python sengfmt2.py in08.txt > 8.txt", shell=True)
if subprocess.call(["diff", "-b", "8.txt", "out08.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 8,  in08.txt -> PASSED", "white"))
else:
	print(colored("Test case 8,  in08.txt -> FAILED", "red"))

#Test case: 9
subprocess.call("python sengfmt2.py in09.txt > 9.txt", shell=True)
if subprocess.call(["diff", "-b", "9.txt", "out09.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 9,  in09.txt -> PASSED", "white"))
else:
	print(colored("Test case 9,  in09.txt -> FAILED", "red"))

#Test case: 10
subprocess.call("python sengfmt2.py in10.txt > 10.txt", shell=True)
if subprocess.call(["diff", "-b", "10.txt", "out10.txt"], stdout=subprocess.DEVNULL) == 0:
	print(colored("Test case 10, in10.txt -> PASSED", "white"))
else:
	print(colored("Test case 10, in10.txt -> FAILED", "red"))

print("===============================")
print("===============================")
print("===============================")
