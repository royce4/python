#!/usr/bin/python
from Tkinter import *
import tkFileDialog, os, shutil
top = Tk()
top.title("Single/MC Ingestion")
top.geometry("400x400")
count=0
Sourcedir=''
Destdir=''

def openDirectory(dirtype):
	dir = tkFileDialog.askdirectory(parent=top, initialdir='/home/', title='Select your directory')
	MoveText(dir,dirtype)

def readycopy():
	empty=''
	if E1.get() <> empty and E2.get() <> empty:
		copystart.config(state=NORMAL)
		#do nothing if not true

def MoveText(dir1,value1):
	if (value1 == 'source'):
		E1.delete(0, END)
		E1.insert(0,dir1)
		var.set("source selected")
		countfiles.config(state=NORMAL) #make count button available
	else:
		E2.delete(0, END)
		E2.insert(0,dir1)
		var.set("destination selected")
	readycopy()

def WriteDir(dir):
	"create log with directory names"
	file=open("log.txt", 'a')
	file.write(dir + '\n')
	file.close()

def copypro(source,destination):
	sourcePath = source
	head,end = os.path.split(sourcePath)
	destPath=destination
#destPath = destination + '\\' + end
#os.mkdir(destPath)
	for root, dirs, files in os.walk(sourcePath):
#figure out where we're going
		dest = destPath + root.replace(sourcePath, '')
#if we're in a directory that doesn't exist in the destination folder
#then create a new folder
		if not os.path.isdir(dest):
			os.mkdir(dest)
			var.set('Directory created at: ' + dest) 
#loop through all files in the directory
		for f in files:
#compute current (old) & new file locations
			oldLoc = root + '\\' + f
			newLoc = dest + '\\' + f
			if not os.path.isfile(newLoc):
				try:
					shutil.copy2(oldLoc, newLoc)
					var.set('File ' + f + ' copied.')
				except IOError:
					var.set('file "' + f + '" already exists')

def countfiles(source):
	"dive to deepest level of a path to find drive file types and number them"
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
				count+=1
				var.set(count + ' sessions in source directory')
			else:
				countfiles(temp_path)
				
lblInst = Label(top, text="Please select Source and Destination", font=("Helvetica", 16))
#and pack it into the window
lblInst.pack()

L1 = Label(top, text="Source:")
E1 = Entry(top)
L1.pack()
E1.pack()
btn1=Button(top, text = "Browse", command = lambda: openDirectory('source'), width = 10)
btn1.pack()
L2= Label(top, text="Destination:")

E2=Entry(top)
L2.pack()
E2.pack()
btn2=Button(top, text="Browse",command = lambda: openDirectory('dest'),width = 10)
btn2.pack()
#copy button
copystart=Button(top,text="Start Copy", command = lambda: copypro(E1.get(),E2.get()), width=10,disabledforeground="#E0E0E0")
copystart.config(state=DISABLED)
copystart.pack(side=BOTTOM)
#count button
countfiles=Button(top,text="Count Sessions", command = lambda: countfiles(E1.get()), width=10,disabledforeground="#E0E0E0")
countfiles.config(state=DISABLED)
countfiles.pack(side=BOTTOM)

var = StringVar()
status = Message( top, textvariable=var, width=200, justify="left", bg="white", fg="blue", relief=RAISED)
var.set("Status....")
status.pack()
#Code to add widgets will go here...

top.mainloop()