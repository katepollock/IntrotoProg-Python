# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
#   KPollock, 11.11.21, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None   # An object that represents a file
strFile = "ToDoList.txt"
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
strTask = "" # Captures task per user
strPriority = "" # Captures priority per user
found = False # Boolean to capture deleted task
dataChange = False # Boolean to capture change in data

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open(strFile, "r")
    for row in objFile:
        t, p = row.split(",")
        dicRow = {"Task": t.strip(), "Priority": p.strip()}
        lstTable.append(dicRow)
    objFile.close()
except FileNotFoundError:
    pass

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? [1 to 5] - ").strip()
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice == '1'):
        if len(lstTable) > 0:
            print(*lstTable[0].keys(), sep=' | ')
            for row in lstTable:
                print(row["Task"], row["Priority"], sep=' | ')
        else: print("No current data to display.")
    # Step 4 - Add a new item to the list/Table
    elif strChoice == '2':
        strTask = input("Enter a task: ")
        strPriority = input("Enter the priority [High, Med, Low]: ")
        lstTable.append({"Task": strTask, "Priority": strPriority})
        print("Task named", strTask.capitalize(), "added.")
        dataChange = True
    # Step 5 - Remove a new item from the list/Table
    elif strChoice == '3':
        strRemove = input("Which item would you like to remove?: ")
        found = False
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
                print("Task Removed")
                found = True
                dataChange = True
        if not found:
            print('Task is not in list.')
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice == '4':
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"]) + '\n')
        print("Data Saved!")
        dataChange = False
        objFile.close()
    # Step 7 - Exit program
    elif strChoice == '5':
        if dataChange:
            dataSave = input("Are you sure you want to exit without saving? [Enter 'yes' or 'no']")
            if dataSave.lower() != 'yes':
                continue
        break  # and Exit the program
    else:
        print(strChoice.capitalize(), "is not an option. Please select [1 to 5].")


