import csv

# number of rows
def get_length(file_path):
	return 1

def append_data(file_path, name, email):
	fieldnames = ['id', 'name', 'email']
	next_id = get_length(file_path)
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	