import csv

def append_data(file_path, name, email):
	fieldnames = ['id', 'name', 'email']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
