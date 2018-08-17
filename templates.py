import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	return file_path
