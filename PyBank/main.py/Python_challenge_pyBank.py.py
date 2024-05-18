#importing the csv and os files
import os
import csv
cwf=os.path.abspath(__file__)

pwd=os.path.dirname(cwf)

budget_csv_path=os.path.join(pwd,"..","Resources","budget_data.csv")



#opening the csv file ,reading the file ,printing out the csv file with header 
row_count=0
total_profit_loss= 0
previous_profit_loss=None
changes=[]
max_profit=0
max_decrease = 0
max_profit_date= None
max_decrease_date =None

with open(budget_csv_path,encoding="UTF-8") as csv_file:
    budget_reader=csv.reader(csv_file, delimiter=",")
    budget_header=next(budget_reader)
    print(f"Budget Header:{budget_header}")

    #calculating total number of rows in the dataset
    for row in budget_reader:
        row_count+=1
    #calculating the net profi/loss 
        profit_loss=int(row[1])
        date = row[0]
        total_profit_loss+=profit_loss
        if previous_profit_loss is not None:
           change=profit_loss-previous_profit_loss
           changes.append(change)
        
           if change>max_profit:
              max_profit= change 
              max_profit_date = date 

           if change<max_decrease:
                 max_decrease = change
                 max_decrease_date = date 

        previous_profit_loss=profit_loss

average_change=sum(changes)/len(changes) 
rounded_average_change=round(average_change,2)
       

print("Financial Analysis")
print("-------------------")
print("                   ")
print(f"Total months: {row_count}")
print("                   ")
print(f"Total: {total_profit_loss}")
print("                   ")
print(f"Average change: ${rounded_average_change}")  
print("                   ")
print(f"Greatest Increase in Profits: {max_profit_date} (${max_profit}) ")
print("                   ")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")  
print("                   ")   

output_path=os.path.join(pwd, "..", "Analysis","financial_analysis.txt")

output_file =open(output_path,"w")

output_file.write("Financial Analysis (Pybank):\n") 

output_file.write("-----------------------------\n\n")
 
output_file.write(f"Total months: {row_count}\n\n" )   

output_file.write(f"Total: {total_profit_loss}\n\n")

output_file.write(f"Average change: ${rounded_average_change}\n\n")

output_file.write(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})\n\n") 

output_file.write("-----------------------------\n\n") 

output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")