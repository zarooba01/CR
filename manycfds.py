import os

def get_dir():
	dir = "D:\\ConsultRisk\\files"
	return dir

def get_all_cfd_txt():
	path = get_dir()
	all_files = []
	for file in os.listdir(path):
		if file.endswith(".txt") and file.startswith("cfd_"): all_files.append(file)

	return all_files
