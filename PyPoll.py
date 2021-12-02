import csv
import os

# Create filepath variable
file_path = os.path.join("Resources", "election_results.csv")

# Open election data file
with open(file_path, 'r') as election_data:
    # Set file reader variable
    file_reader = csv.reader(election_data)

    # Skip header row
    header = next(file_reader)
    print(header)

    #for row in file_reader:
    #    print(row)

# go through file and check for unique name,
    #if unique add to list with vote

    #if not unique add vote to existing name

file_path_results = os.path.join("Analysis", "election_anaylsis.txt")

# Open election anaylsis file
with open(file_path_results, "w") as election_results:

    election_results.write("Arapahoe\nDenver\nJefferson")
    

    print(election_results)