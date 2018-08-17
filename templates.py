import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception(f"{file_path} is not a valid template path...")
	return file_path


def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()


print(get_template(r'templates\email_message.txt'))
