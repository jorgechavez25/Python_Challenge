#import csv file / read from it
import os
import csv

absolute_path = os.path.dirname(__file__)
election_data = os.path.join(absolute_path,"Resources", "election_data.csv")

#list to store data/set variables
candidates = []

per_can = {}

vote_counter = 0

winning_can = ""

win_counter = 0


#open file as csv file
with open(election_data,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    for row in csvreader:

        #add vote to counter
        vote_counter = vote_counter + 1

        #get total candidate
        candidates_name = row[2]

        #add new candidate if not added
        if candidates_name not in candidates:

            candidates.append(candidates_name)

            #track votes in counter
            per_can[candidates_name] = 0

        #add votes to counter per candidate
        per_can[candidates_name] = per_can[candidates_name] + 1

        #print vote count
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {vote_counter}")
    print("---------------------")

  
        #determine winner 
    for candidate in per_can:

        #write vote count and percentage

        votes = per_can.get(candidate)
        vote_per = float(votes) / float(vote_counter) * 100

        #show winning count and candidate
        if (votes > win_counter):
            win_counter = votes
            winning_can = candidate

        #results of canditdates/print results of candidates

        voter_results = f"{candidate}: {vote_per:.3f}% ({votes})"
        print(f"{voter_results}")

        #results for winning candidate
    winning_results = f"Winner: {winning_can}"
        
    print("---------------------")
    print(f"{winning_results}")
    print("---------------------")
         
         
  #export as txt file
    output_path = os.path.join(absolute_path,"Analysis", "electionanalysis.txt")
    #specify where to hold contents
    with open(output_path,"w") as file:
        #intialize cs.writer
                #csvwriter = csv.writer(file,delimiter=',')
        #first row
                file.write("Election Results\n")
        #second row
                file.write("---------------------\n")
        #third row
                file.write(f"Total Votes: {vote_counter}\n")
        #fourth row
                file.write("---------------------\n")        
        #fifth row
                for candidate in per_can:

        #write vote count and percentage
                    votes = per_can.get(candidate)
                    vote_per = float(votes) / float(vote_counter) * 100

        #show winning count and candidate
                    if (votes > win_counter):
                        win_counter = votes
                        winning_can = candidate
                    #results of canditdates/print results of candidates
                    voter_results = f"{candidate}: {vote_per:.3f}% ({votes})\n"
                    file.write(f"{voter_results}\n")
        #sixth row
                file.write("---------------------\n")
        #seventh row
                file.write(f"{winning_results}\n")
        #eighth row
                file.write("---------------------\n")

        
        
    
        
        

        







    
          
