import csv
import os

# Directory containing all CSV files
script_directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(script_directory, 'results')
# Output file name for the merged CSV
output_file = 'merged.csv'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Write the header from the first CSV file to the output file
first_csv = csv_files[0]
with open(os.path.join(directory, first_csv), 'r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Read the header from the first CSV

# Write data from all CSV files (excluding headers) to the output file
with open(os.path.join(directory, output_file), 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)  # Write header to the output file
    for csv_file in csv_files:
        if csv_file != first_csv:
            with open(os.path.join(directory, csv_file), 'r', newline='') as infile:
                next(infile)  # Skip the header
                for line in infile:
                    writer.writerow(line.strip().split(','))  # Write data to the output file
