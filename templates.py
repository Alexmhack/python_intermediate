import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception(f"{file_path} is not a valid template path...")
	return file_path


def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()


template_text = get_template(r'templates\email_message.txt').format(
	name='Pranav',
	date='15th Aug, 18',
	total=560
)

print(template_text)
