import csv
import requests

with open('roster2.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	for row in csv_reader:
		data = {
			"first name": row[0],
			"last name": row[1]
		}
		response = requests.post('http://localhost:5000/api/member', json=data)
		json_response = response.json()
		print(data, json_response)

