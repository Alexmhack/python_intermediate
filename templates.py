import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if os.path.isfile(file_path):
		raise Exception("This is not a valid template path...")
	return file_path
