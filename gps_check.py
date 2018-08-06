import os,sys

def GPSCheck(file_path):
	"check GPS file is present and not empty"
	check_list=[]
	temp_path = "gps"
	gps_path=os.path.join(file_path,temp_path)
	check_list=os.listdir(gps_path)
	if len(check_list) > 0:
		for file in check_list:
			if file.endswith(".gps"): # find GPS file
				gpsFilePath=os.path.join(gps_path,file)
				sizegps=os.path.getsize(gpsFilePath) #obtain size of file. if 0 then not valid
				if sizegps > 0:
					with open(gpsFilePath, "r") as f: #read gps file check if format is valid
						data=f.readlines()
						ValidGps=1
						enumerate_object = enumerate(data)
						for index,line in enumerate_object:
							words=line.split(",")
							if len(words) <> 10:
								ValidGps=0
								print "invalid GPS data at line: " + str(index+1)
					if ValidGps:
						print "valid! " + file
					else:
						print "INVALID! " + file
				else:
					print "Empty GPS file! " + file
	else:
		print "no GPS files in " + file_path + " Invalid!"

input_path= sys.argv[1]
GPSCheck(input_path) #put in top level path to drive file
print('all done')