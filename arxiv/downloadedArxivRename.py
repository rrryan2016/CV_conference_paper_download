import requests
from bs4 import BeautifulSoup
import os
import sys

def main(folder_path=None):
	files = [i for i in os.listdir(folder_path) if not os.path.isdir(i)] # Ignore subdirectories
	for filename in files:
		# print(filename[:-4])
		# filename 
		page = requests.get("https://arxiv.org/abs/"+filename[:-4]) # https://arxiv.org/abs/1910.05401
		if page.status_code == 200: # Check if website exists
			soup = BeautifulSoup(page.content,'html.parser')
			tags = soup.find("h1","title mathjax")
			x = list(tags)
			file_name = str(x[1].strip())
			file_name = file_name.replace(" ","_")
			file_name = file_name.replace("-","_")
			file_name = file_name+'.pdf'
			
			os.chdir(folder_path)
			print('Renaming {} to {} ...'.format(filename,file_name))
			# os.rename(filename,file_name)


			# print (os.path.exists(os.path.join(folder_path,filename)))
			# # os.rename(str(sys.argv[1])+filename,str(file_name))
			# print('Renaming {} to {} ...'.format(os.path.join(folder_path,filename),os.path.join(folder_path,file_name)))
			# print('new folder: ',os.path.join(folder_path[:-6],file_name))
			os.rename(os.path.join(folder_path,filename),os.path.join(folder_path[:-6],file_name))
		else:
			print ("Not an arxiv paper!")

if __name__=="__main__":
	folder_path = '/data/amax/users/liuwenzhe/paper/lily_202102/Texture Classification in Extreme Scale Variations using GANet/arxiv'
	# folder_path = folder_path.replace('\','/')
	# print('new folder_path: ',folder_path)
	main(folder_path=folder_path)