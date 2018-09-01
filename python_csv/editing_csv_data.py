import csv
import shutil

from tempfile import NamedTemporaryFile

FILE_NAME = 'data.csv'
temp_file = NamedTemporaryFile(delete=False)

with open(FILE_NAME, 'wb', , newline='') as csvfile, temp_file:
	reader = csv.DictReader(csvfile)
	fieldnames = ['id', 'name', 'email', 'amount', '']
	writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
	writer.writeheader()

	for row in reader:
		writer.writerow({
			"id": row["id"],
			"name": row["name"],
			"email": row["email"],
			"amount": "599.99",
			"sent": ""
		})
