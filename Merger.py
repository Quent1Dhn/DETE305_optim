import csv
import os

# Directory containing all CSV files
script_directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(script_directory, 'results_avec_gaz')

# Output file name for the merged CSV
outputdir=os.path.join(script_directory, 'resultats_combines')
output_file = 'Resultats_combines_gaz_75.csv'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

first_csv = csv_files[0]

# Write data from all CSV files (excluding headers) to the output file
with open(os.path.join(outputdir, output_file), 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for csv_file in csv_files:
        if csv_file != first_csv:
            with open(os.path.join(directory, csv_file), 'r', newline='') as infile:
                next(infile)
                next(infile)   # Skip the header
                for line in infile:
                    writer.writerow(line.strip().split(','))  # Write data to the output file
        else :
            with open(os.path.join(directory, csv_file), 'r', newline='') as infile:
                for line in infile:
                    writer.writerow(line.strip().split(','))  # Write data to the output file

