#PERSONAL EXPENSE TRACKER
import csv

csv_file='expenses.csv'

#function to start the file/initialize csv
def intitializeCSV():
    try:
        file=open(csv_file,"w")
        writer=csv.writer(file)
        writer.writerow(['date','category','description','amount'])
        file.close()
    except FileExistsError:
        pass #no intitialion because file alredy exists

intitializeCSV()   
#function to record the expenses
def recordExpenses():
    print('50')
    inp_date=input("enter the date:")
    inp_category=input("enter the categry:")
    inp_desc=input("enter the description:")
    inp_amt=float(input("enter the amount:"))
    print("_"*50)

    #storing the above data in the csv file
    file=open(csv_file,mode='a')
    writer=csv.writer(file)
    writer.writerow([imp_date,imp_category,imp_desc,imp_amt])
    print("expenses addded successfully")
    file.close()
    
#function to show the expenses
def showExpenses():
    try:
        with open(csv_file,mode='r')as file:
            reader=csv.reader(file)
            next (reader)
            for row in reader:
                print(row)
    except:
        print("no content found")

#function displayvarious operations
def options():
    print("-"*50)
    print("select the option to chose operation")
    print("1.record expense")
    print("2.show expenses")

    option = int(input("enter your choice:"))
    return option


#function to handle the entireprogram
def main():
    choice='y'
    while choice=='y':
        opt=options()
        if opt==1:
            recordExpenses()
        elif opt==2:
            showExpensed()
        else:
            print("--invalid option can't you see!!")

            choice=input("do you want to continue?(type ""y" "for yes)")
            print("\n**The program close here**\n")
main()













            
