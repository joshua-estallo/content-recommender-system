import csv

# Define the path to your CSV file
csv_file_path = "output.csv"

# Read the existing data from the CSV file
existing_data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        existing_data.append(row)

# Add the new column header to the first row
existing_data[0].append("id")

# Add values to the "dataset id" column starting from the second row
for i, row in enumerate(existing_data[1:], start=1):
    row.append(str(i))  # Values 1, 2, 3, ... for each row

# Open the CSV file in write mode and write the updated data
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(existing_data)

print("New column 'dataset id' added successfully.")
