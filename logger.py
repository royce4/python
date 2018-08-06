# A first Python script
import os,sys,glob                  # Load a library module

def CreateLog
	"create a log file"
	pass
def WriteLog
	"append to log file"
	pass
def WriteDir(dir):
	"create log with directory names"
	file=open("log.txt", 'a')
	file.write(dir + '\n')
	file.close();

def GPSCheck(file_path):
	"check GPS file is present and not empty"
	check_list=[]
	temp_path = /gps
	gps_path=os.path.join(file_name,temp_path)
	check_list=os.listdir(gps_path)
	for file in check_list:
		if file.endswith(".gps"):
			sizegps=os.path.getsize()
			print sizegps

def ImageCheck(file_path)
	"check Images folder"
	check_list=[]
	temp_path = /images
	images_path=os.path.join(file_name,temp_path)
	pass

def PathDive(path_name):
	"dive to deepest level of a path to find drive file type"
	e=os.listdir(path_name)
	valid_tup=('gps','images')
	drive_list=[]
	check_list=[]
	#print e
	for file in e:
		if os.path.isdir(os.path.join(path_name,file)):
			temp_path=os.path.join(path_name,file)
			check_list=os.listdir(temp_path)
			valid=(valid_tup[0] in check_list) and (valid_tup[1] in check_list)
			if valid:
				WriteDir(temp_path)
			else:
				PathDive(temp_path)
	return
	
input_path= sys.argv[1]
PathDive(input_path)
print('all done')
