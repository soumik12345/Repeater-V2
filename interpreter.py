import re
import os
import subprocess

stackMemory=[]

def create_file(address):
	f=open(address, "r")
	f.close()
	path=r'C:\Program Files\Microsoft VS Code\Code.exe'
	subprocess.Popen("%s %s" % (path, address))

def generate_lines(address):
	f_open=open(address, "r")
	lines=str(f_open.read()).split('\n')
	return lines

def generate_opcode_line(opCodes):
	address="opcodes.txt"
	f=open(address, "w")
	for i in opCodes:
		f.write(str(i)+str('\n'))
	f.close()

def generate_token(lines):
	arr=lines[0].split('=')
	return arr[len(arr)-1].strip()

def generate_opcode(lines):
	regex, opcode, opinit=r''+token, [], 0
	for i in range(1, len(lines)):
		if lines[i].find("rip")!=-1:
			opcode.append(0)
			continue
		elif lines[i].find("op_a")!=-1:
			opinit=0
		elif lines[i].find("op_b")!=-1:
			opinit=10
		elif lines[i].find("op_io")!=-1:
			opinit=20
		elif lines[i].find("op_log")!=-1:
			opinit=30 
		arr=re.findall(regex, lines[i])
		opcode.append(int(len(arr)+opinit))
	return opcode

def interpret(opCodes):
	i, memory=0, []
	while i<len(opCodes):
		if opCodes[i]==0:
			quit()
		
		elif opCodes[i]==1:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				stackMemory.append(str(float(topnext)+float(top)))
			else:
				stackMemory.append(topnext+top)

		elif opCodes[i]==2:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				stackMemory.append(str(float(topnext)-float(top)))
			else:
				print("Subtraction not possible")

		elif opCodes[i]==3:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				stackMemory.append(str(float(topnext)*float(top)))
			else:
				print("Multiplication not possible")	

		elif opCodes[i]==4:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				stackMemory.append(str(float(topnext)/float(top)))
			else:
				print("Division not possible")

		elif opCodes[i]==5:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				stackMemory.append(str(float(topnext)%float(top)))
			else:
				print("Modulus not possible")

		elif opCodes[i] == 11:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top == topnext:
				stackMemory.append("1")
			else:
				stackMemory.append("0")	

		elif opCodes[i] == 12:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				if float(top) > float(topnext):
					stackMemory.append("1")
				else:
					stackMemory.append("0")	
			else:
				print("Invalid Operation")					

		elif opCodes[i] == 13:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				if float(top) < float(topnext):
					stackMemory.append("1")
				else:
					stackMemory.append("0")
			else:
				print("Invalid Operation")	

		elif opCodes[i] == 14:
			top=str(stackMemory[len(stackMemory)-1])
			topnext=str(stackMemory[len(stackMemory)-2])
			if top.isdigit() and topnext.isdigit():
				stackMemory.append(float(top) & float(topnext))
			else:
				print("Invalid Operation")
		elif opCodes[i] == 15:
			top=str(stackMemory[len(stackMemory)-1])
			if top.isdigit():
				x = float(top)
				r = not x
				stackMemory.append(str(int(r))) 
			else:
				print("Invalid Operation")													

		elif opCodes[i]==21:
			stackMemory.append(input())

		elif opCodes[i]==22:
			print(stackMemory[len(stackMemory)-1])

		# elif opCodes[i]==23:
			

		i+=1

# Driver code
print("Enter address of the file: ", end="")
address=input()
# create_file(address)
lines=generate_lines(address)
token=generate_token(lines)
opCodes=generate_opcode(lines)
print(opCodes)
generate_opcode_line(opCodes)
interpret(opCodes)