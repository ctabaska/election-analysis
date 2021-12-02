import csv
import os

# Create filepath variable
file_path = os.path.join("Resources", "election_results.csv")


total_votes = 0
candidate_votes = {}

# Open election data file
with open(file_path, 'r') as election_data:
    # Set file reader variable
    file_reader = csv.reader(election_data)

    # Skip header row
    header = next(file_reader)
    #print(header)

    for row in file_reader:

        # Check candidate name and add to dictionary if not in dictionary already
        candidate_name = row[2]
        if candidate_name not in candidate_votes.keys():
            candidate_votes[candidate_name] = {'votes': 1, 'percentage': 0.0}
        else:
            candidate_votes[candidate_name]['votes'] += 1

        # Total the votes
        total_votes += 1

    # Check percentage of votes for each candidate
    for candidate in candidate_votes:
        candidate_votes[candidate]['percentage'] = float(candidate_votes[candidate]['votes']) / float(total_votes) * 100

# print candidate data
#for candidate in candidate_votes:
#    print(f"{candidate}: {candidate_votes[candidate]['percentage']:.1f}% ({candidate_votes[candidate]['votes']:,})")

winning_candidate = {'name': '', 'votes': 0, 'percentage': 0}

# Find winner
for candidate in candidate_votes:
    if (candidate_votes[candidate]['votes'] > winning_candidate['votes']):
        winning_candidate['name'] = candidate
        winning_candidate['votes'] = candidate_votes[candidate]['votes']
        winning_candidate['percentage'] = candidate_votes[candidate]['percentage']

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate['name']}\n"
    f"Winning Vote Count: {winning_candidate['votes']:,}\n"
    f"Winning Percentage: {winning_candidate['percentage']:.1f}%\n"
    f"-------------------------\n")

#print(winning_candidate_summary)

file_path_results = os.path.join("Analysis", "election_anaylsis.txt")

# Open election anaylsis file
with open(file_path_results, "w") as election_results:

    results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(results, end="")
    # Save the final vote count to the text file.
    election_results.write(results)

    for candidate in candidate_votes:
        candidate_result = (
            f"{candidate}: {candidate_votes[candidate]['percentage']:.1f}% ({candidate_votes[candidate]['votes']:,})\n"
        )
        print(candidate_result)
        election_results.write(candidate_result)
    
    election_results.write(f"-------------------------\n")

    print(winning_candidate_summary)
    election_results.write(winning_candidate_summary)
    #print(election_results)