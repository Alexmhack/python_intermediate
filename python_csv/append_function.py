import csv

# number of rows
def get_length(file_path):
	return 1

def append_data(file_path, name, email):
	fieldnames = ['id', 'name', 'email']
	next_id = get_length(file_path)
	with open('data.csv', 'a') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({
			"id": next_id,
			"name": name,
			"email": email
		})
