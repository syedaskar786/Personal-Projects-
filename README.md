Personal Expense Tracker 

Having a good spending habit is essential to maintaining a healthy personal financial status. To facilitate the process, a personal expense tracker may help, which is an application that helps users to keep track of their income and spendings, as well as allocating the money systemically for various purposes (e.g., saving, investment and charity). Using Python, we can implement a Personal Expense Tracker application. This program allows its user to input their income(s), spendings and other allocations. Here are the functions of the system: 

i. Input/store/update/retrieve the income(s), spendings and other allocations 
ii. Display the total income of last year 
iii. Display the top three spendings in the past 30 days 
iv. Display the percentages of each category of expenditure (Utilities, Housing, Transportation, Others)

Data Abstraction: 
Some of the key data types of python are Numeric (Integers and Float), Sequence (String, List, Tuple), Boolean, Set, and Dictionary. Some examples of the above data types are: 
•	Numeric: 
o	Integer:   x = 5

o	Float:       x = 5.0

•	Sequence: 
o	String:    x = “hello world”
o	List:         x = [‘Hello’, ‘world’]
o	Tuple:      x = (‘Hello’, ‘world’)

•	Boolean: 
o	x = True

•	Set: 
o	x = set ( ["Hello", "world"] ) 

•	Dictionary: 
o	x = {'Hello': 'world', 1: [5, 2,7, 4]} 

•	Some of the data types we used in our program are: 
o	Int
o	Float
o	date (using datetime)
o	boolean 
o	list

A Python; implementation of the data types:
•	Boolean:
o	filtered_df=filtered_df.sort_values(by=['Amount'],ascending=False).reset_index(drop=True)  (Line code: 112) 
o	In this line of code we are using the boolean function() to ascend the values according to their weightage in order to find the top 3 spending in the past 30 days. This helps us with identifying situation which are true and false by executing values they are assigned. 


•	 Numeric:
o	int: choice = int(input("Please enter number 0-4:"))   (Line code:16)
o	We are using the int function() to enter the numeric value from 0 to 4 in order to select the service we want to update. It helps us in entering integers to a string. 
o	float: profit = float(input("Amount of Income: "))  (Line code:21)
o	We are using the float function() here to add the new value to the update the service. The function allows us to enter value with decimals as well

•	Date:
o	dates = date.today()  (Line code:22)
o	We use the date function() to add the date of the day we enter value to our Income section. This function helps us in adding dates to our incomes, expenses, and spendings. 

•	Dictionary:
o	x = df.loc[i, ['Type']]  (Line code:130)
o	This dictionary function() allows us to access the multiple lines of columns in order to determine the type of the service that we are calling on. This functions helps us save time by creating several for loops to look for each column one by one. 

•	Sequences:
o	String:    event = input("Income name: ")  (Line code:20)
o	The string function() allows us to enter the source of income we are generating or receiving. This help us in adding names of the source of incomes easily. 
o	List:       expense_service = []      (Line code:4)
o	This list function() allows us add values to the expense service in future. We create it at the start of code in order to list out all the variable we will be using in our code. This makes it easier for us to call it in future references. 

A modular design of the program via the definition and use of a few key functions/procedures: 
Our program includes four functions, one for each of the functions of our program. We call these functions in the main() section of our code. The four functions are: 
•	update():
o	 The function update() inputs, stores, modifies and retrieves income and expenditure data. The data collected is stored into two csv files-- one for income and one for expenditure. 

•	total_Income(): 
o	The Function total_icome() takes into account the income that you receive based on your input such as Job salary, Business, and Savings etc.It produces a final report in which it adds up the input data (Income) and print it out as the total income.

•	get_top_three(): 
o	The function get_top_three() goes through all the expenses and takes the last 30 days expenses, then search for the highest expenses and print the top 3 spendings out

•	categorize():
o	 catergorize() goes through every element in the file that stores the expenses, checks the type of every value in the file, categorizes the expenses and displays the percentages of each category spent

Special Observation:
•	Through this project, I explored many new properties. In particular, I learned the usage of the properties .loc[] and and .at[]. I learned how .loc[] can be used to access multiple rows or multiple columns while .at[] is used to access a single element. I also tried using .iloc[] during the process of writing the program which is used based on the integer position of elements. 



