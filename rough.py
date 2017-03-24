import os
dir_path = os.path.dirname(os.path.realpath(__file__))
fileList = os.listdir(dir_path+"\\Shares")

with open(dir_path + '\\asdf.txt', 'a') as the_file:
	for file in fileList:
		the_file.write(file[:-4] + '\n')