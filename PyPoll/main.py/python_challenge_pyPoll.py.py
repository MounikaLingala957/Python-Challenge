#yPoll Analysis:
# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

import os 
import csv
cwf = os.path.abspath(__file__)
cwd=os.path.dirname(cwf)
election_csv_path=os.path.join(cwd,"..","Resources","election_data.csv")

#Global variables:
row_count= 0
candidate_list=[]
candidate_votes={}
a =0
b=0
c=0

#opening csv file and setting up header row 

with open(election_csv_path,"r",encoding="UTF-8") as csv_file:
    election_reader=csv.reader(csv_file,delimiter=",")
    election_header=next(election_reader)
    print(f"Election_Header {election_header}")

    #Total number of votes cast 
    for row in election_reader:
        row_count+=1 
    #Unique list of candidates
        candidate=row[2]
        if row[2] not in candidate_list:
             candidate_list.append(row[2])

    #votes casted for each candidate
        if row[2] ==candidate_list[0]:
            a+=1
        elif row[2]==candidate_list[1]:
            b+=1
        else: 
            row[2]==candidate_list[2]
            c+=1
        
           
#calculate percentage of votes casted
def calculate_percentage(m,n,o): 
    y=row_count
    return (round((m/y)*100),round((n/y)*100),round((o/y)*100))
percentage_list=calculate_percentage(a,b,c)

candidate_voting = dict(zip(candidate_list,[a,b,c]))

#comparing for Winner
value=0
for key in candidate_voting:
    if candidate_voting[key]>value:
        value=candidate_voting[key]
for key in candidate_voting:
    if value ==candidate_voting[key]:
       winner=key   

#printing out the results to the terminal:     
print()
print(f"Total votes : {row_count}")
print()
print(f"{candidate_list[0]} :{percentage_list[0]}% ({a})")
print()
print(f"{candidate_list[1]} :{percentage_list[1]}% ({b})")
print()
print(f"{candidate_list[2]} :{percentage_list[2]}% ({c})")
print()
print(f"Winner:{winner}")
print()


#Printing results to a text file in Analysis Folder:
output_path=os.path.join(cwd, "..", "Analysis","election_results.txt")

output_file =open(output_path,"w")

output_file.write("Election Results (PyPoll) :\n") 

output_file.write("-----------------------------\n\n")
 
output_file.write(f"Total votes : {row_count}\n\n" )   

output_file.write(f"{candidate_list[0]} : {percentage_list[0]}%  ({a})\n\n")

output_file.write(f"{candidate_list[1]} : {percentage_list[1]}%  ({b})\n\n")

output_file.write(f"{candidate_list[2]} : {percentage_list[2]}%  ({c})\n\n") 

output_file.write("-----------------------------\n\n") 

output_file.write(f"Winner: {winner}")