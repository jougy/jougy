import os
import shutil
import pyautogui

path = "/Users/João Paulo do Val/Desktop/fast folder Local/"
names = os.listdir(path)
folder_name = ["QrCode","python"]
for x in range(0,4):
	if not os.path.exists(path+folder_name[x]):
		os.makedirs(path+folder_name[x])
for files in names:
	if ".png" in files and not os.path.exists(path+"QrCode/"+files):
		shutil.move(path+files, path+"QrCode/"+files)
for files in names:
	if ".py" in files and not os.path.exists(path+"python/"+files):
		shutil.move(path+files, path+"python/"+files)



