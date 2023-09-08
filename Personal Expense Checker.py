from datetime import date, timedelta
import pandas as pd

expense_service = []
expense_price = []
expense_date = []
expense_stype = []
income_event = []
income_profit = []
income_date = []
income_etype = []
income = {}
expense = {}
def update():
    print("0) menu\n1) Income\n2) Expense\n3) Update\n4) Retrieve values")
    choice = int(input("Please enter number 0-4:"))
    if choice == 0:
        return main()
    elif choice == 1: #to add income element to file
        event = input("Income name: ")
        profit = float(input("Amount of Income: "))
        dates = date.today()
        income_event.append(event) #the name of the income source
        income_profit.append(profit) #the amount of the income
        income_date.append(dates) #the date of receiving the income
        income["Income"] = income_event
        income["Amount"] = income_profit
        income["Date"] = income_date
        income_report = pd.DataFrame(income) #storing the data in a file
        income_report.to_csv("income.csv")
        print(income_report, end="\n")
        print("\n")
        return update()
    elif choice == 2: #to add expense element to file
        service = input("Expense name: ") #the name of the expense
        price = float(input("price: ")) #the amount spent
        dates = date.today() #the date of the spending
        stype = ""
        while True:
            stype = input("Type of expense (Utilities/ Housing/ Transportation/ Others): ")
            if stype == "Utilities" or stype=="utilities" or stype == "Housing" or stype == "housing" or stype == "Transportation" or stype == "transportation" or stype == "Others" or stype == "others":
                break
            else:
                print("Please enter valid input: ")
        expense_service.append(service) #storing the values in a list
        expense_price.append(price)
        expense_date.append(dates)
        expense_stype.append(stype)
        expense["Expense"] = expense_service #storing the values in the columns of the data file
        expense["Amount"] = expense_price
        expense["Date"] = expense_date
        expense["Type"] = expense_stype
        expense_report = pd.DataFrame(expense)
        expense_report.to_csv("expense.csv")  #storing the data in a file
        print(expense_report, end="\n")
        print("\n")
        return update()
    elif choice == 3: #to modify the values of income or expense
        change = input("Would you like to change the values of income or expenses? ")
        if change == "income" or change == "Income":
            change_ind = int(input("Enter the index of the Income value that needs to be changed: "))
            new_amt = input("Enter the new amount: ")
            income_report = pd.DataFrame(income)
            income_report.at[change_ind, ['Amount']] = [new_amt]
            print(income_report, end="\n")
        elif change == "expenses" or change == "Expenses":
            change_ind = int(input("Enter the index of the Expense value that needs to be changed: "))
            new_amt = input("Enter the new amount: ")
            expense_report = pd.DataFrame(expense)
            expense_report.at[change_ind, ['Amount']] = [new_amt]
            print(expense_report, end="\n")
        print("\n")
        return update()
    elif choice == 4: #to retrieve and view values from income or expenses
        ret = input("Would you like to retrieve values from income or expenses? ")
        if ret == "income" or ret == "Income":
            ret_ind = int(input("Enter the index value of the element you would like to retrieve: "))
            income_report = pd.DataFrame(income)
            print(income_report.loc[[ret_ind]])
        elif ret == "expenses" or ret == "Expenses":
            ret_ind = int(input("Enter the index value of the element you would like to retrieve: "))
            expense_report = pd.DataFrame(expense)
            print(expense_report.loc[[ret_ind]])
        print("\n")
        return update()
    else:
        print("\n")
        return update()

'''The function update() inputs, stores, modifies and retrieves income and expenditure data. The data collected is stored into two csv files-- one for income and one for expenditure. 
'''

def total_Income():#This function is to find the total income 
    input = pd.read_csv('Income.csv')# it allows the program to read the csv file to gather data already stored on it 
    df = pd.DataFrame(input)#dataframe for rows and coloums used to find the data values for finding total income.\
    sum = 0 #stores the total sum of income during the last year
    for i in range(len(df)): #to go through each element in the data file
        if (i == (len(df))-2 or i == len(df)-1):
            sum = sum + df.loc[i, ['Amount']]#sum gets added by adding each value store in coloums
    print("The Total Income of last year is ", sum)#prints out the total income 
    print("\n")
    return main()

"""
The Function total_icome() takes into account the income that you receive based on your input such as Job salary, Business, and Savings etc.
It produces a final report in which it adds up the input data (Income) and print it out as the total income.
"""

def get_top_three():
    df = pd.DataFrame(expense)# it allows the program to read the csv file to gather data already stored on it 
    filtered_df = df[df.Date > (date.today() - timedelta(days=30))] #the data of the last 30 days
    filtered_df = filtered_df.sort_values(by=['Amount'], ascending=False).reset_index(drop=True)
    results_df = filtered_df.loc[0:2, :]
    print(results_df) #the top three spendings in the last 30ndays
    print("\n")
    return main()

'''The function get_top_three() goes through all the expenses and takes the last 30 days expenses, then search for the highest expenses and print the top 3 spendings out'''

def categorize():
    df = pd.DataFrame(expense)
    print(df, end="\n")
    len_file = len(df.index)
    uti = 0  # Stores the total amount spent on utilities
    house = 0  # Stores the total amount spent on housing
    transpo = 0  # Stores the total amount spent on transportation
    other = 0  # Stores the total amount spent on others
    file_sum = 0  # Stores total spening
    for i in range(0, len_file):
        x = df.loc[i, ['Type']]
        x1 = ''.join(x)
        if x1 in ["Utilities", "utilities"]:
            x2 = float(df.loc[i, ['Amount']])
            uti += x2
        elif x1 == "Housing" or x1 == "housing":
            x2 = float(df.loc[i, ['Amount']])
            house += x2
        elif x1 == "Transportation" or x1=="transportation":
            x2 = float(df.loc[i, ['Amount']])
            transpo += x2
        elif x1 == "Others" or x1=="others":
            x2 = float(df.loc[i, ['Amount']])
            other += x2
        file_sum = file_sum + float(df.loc[i, ['Amount']])
    uti_percent = (uti / file_sum) * 100  # Stores the percentage of amount spent on utilities
    house_percent = (house / file_sum) * 100  # Stores the percentage of amount spent on housing
    transpo_percent = (transpo / file_sum) * 100  # Stores the percentage of amount spent on transportation
    other_percent = (other / file_sum) * 100  # Stores the percentage of amount spent on others
    print("The percentage of income spent on Utilities is : ", uti_percent, "%")
    print("The percentage of income spent on Housing is : ", house_percent, "%")
    print("The percentage of income spent on Transportation is : ", transpo_percent, "%")
    print("The percentage of income spent on Others is : ", other_percent, "%")
    print("\n")
    return main()

'''
The function catergorize() goes through every element in the file that stores the expenses, checks the type of every value in the file, categorises the expenses and displays the percentages of each category spent
'''


def main():
    print("Menu:\n0) Quit\
    \n1) Input/store/update/retrieve the expense(s), spendings and other allocations\
\n2) Display the total Income of last year\
\n3) Display the top three spendings in the past 30 days\
\n4) Display percentages of the categories of money spent\n")
    choice = int(input("Please enter number 0-4:"))
    print("\n")
    if choice == 0:
        print("quit")
    elif choice == 1:
        update()
    elif choice == 2:
        total_Income()
    elif choice == 3:
        get_top_three()
    elif choice == 4:
        categorize()
    else:
        return main()


main()
