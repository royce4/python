#!/usr/bin/python3

import os,sys,datetime

class LegacyDrive:
	pass

def PathDive(path_name):
	"dive to deepest level of a path to find drive file type"
	e=os.listdir(path_name)
	
	pass

def CheckValid(path_name):
	"check the validity of a drive file. Meaning does it have appropriate sub-folders"
	e=os.listdir(path_name)
	drives=()
	#file is file name, e is list of file names
	valid_tup=('gps','images')
	for element in valid_tup:
	valid_list=['gps','images'] #check if valid if there is a GPS AND Images folder structure
	for file in e:
		if os.path.isdir(os.path.join(path_name,file)):
			check_list=os.listdir((os.path.join(path_name,file)))
			for element in valid_tup:
				valid=valid_tup[i] in check_list
			if valid:
				drives.append((os.path.join(path_name,file))
				print file + " is valid" + '\n'
			else:
				print file + " is not valid" + '\n'
		del check_list[:]
			
def GetFileNames(directory):
	"when given a directory name return the names of the sub-directories in a list"
	print "accessing" , directory
	dirs = os.listdir(directory)
	print dirs
	print '\n'
	return dirs;
	
def listdir_fullpath(d):
	"given a path write sub-directories and path in csv"
	file=open("paths.csv", 'a')
	e=os.listdir(d)
	#f is file name, e is list of file names, d is the directory
	for f in e:
		if os.path.isdir(os.path.join(d,f)):
			file.write(f + ',' + os.path.join(d,f) + '\n')
   # return [os.path.join(d, f) for f in os.listdir(d)]
	file.close();

def WriteDir(path):
	"create log with directory names"
	file=open("log.txt", 'a')
	for x in range(len(path)):
		file.write(path[x] + '\n')
	file.close();

print("Heel Toe University LLC")
input_path= sys.argv[1]
WriteDir(GetFileNames(input_path))
file=open("log.txt", 'r')
str=file.read();
print (str)
file.close()
pat=listdir_fullpath(input_path)
print '\n'
CheckValid(input_path)
print('all done')