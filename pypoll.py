#pseudocode
    #1. The total number of votes cast
    #2. a complete list of candidates who received votes
    #3. the percentage of votes each candidate won
    #4. the total number of votes each candidate won
    #5. the winner of the election based on popular vote  
    
    
#section 3.4.2 on reading data
                # #The data we need to retrieve
                # import csv
                # import os
                # # Assign a variable for the file to load and the path.
                # #file_to_load = '/Users/jenniferklein/Documents/Analytics Bootcamp/Online Lesson Projects/Module3_Election-Analysis/resources/election_results.csv'
                # file_to_load = os.path.join("/Users/jenniferklein/Documents/Analytics Bootcamp/Online Lesson Projects/Module3_Election-Analysis/resources", "election_results.csv")

                # # Open the election results and read the file
                # with open(file_to_load) as election_data:
                #      # To do: perform analysis.
                #      print(election_data)

#section 3.4.3 on writing data
# import csv
# import os
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("/Users/jenniferklein/Documents/Analytics Bootcamp/Online Lesson Projects/Module3_Election-Analysis/analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file.
#      txt_file.write("Arapahoe")

#section 3.4.4
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/jenniferklein/Documents/Analytics Bootcamp/Online Lesson Projects/Module3_Election-Analysis/resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/jenniferklein/Documents/Analytics Bootcamp/Online Lesson Projects/Module3_Election-Analysis/analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # read the file object with the reader function. 
    file_reader = csv.reader(election_data)
    #print header row
    headers = next(file_reader)
    print(headers)
        #print each row in the CSV file. 
    # for row in file_reader:
    #     print(row)




