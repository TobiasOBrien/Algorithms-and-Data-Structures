# Tobias O'Brien
# CS499-CS260
# Nov/ Dec 2021

# Goal of the program is to recreate artifacts from CS260 that were originally written in C++
# Import CSV
# Display full dataset
# List Departments and number of records
# Search for specific Department records
# Search for records by Net Sales (Lowest)
# Search for records by Auction Title Keyword
# Show Department Totals

import pandas as pd

# variables
df = "Make sure you load the file first."  # Used to define df as a global variable

# User menu layout
menu_options = {
    1: 'Load CSV file',
    2: 'Display full dataset',
    3: 'List Departments and Number of Records',
    4: 'Search for Department Records',
    5: 'Search for Records by Net Sales',
    6: 'Search for Records by Auction Keyword',
    7: 'Show Department Totals',
    8: 'Search for a specific Auction ID',
    9: 'Exit',
}


# Define the user menu
def print_menu():
    print()
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    print()


# Define option 1 - Load the CSV File
def option1():
    global df
    df = pd.read_csv(r'eBid_Monthly_Sales.csv')
    row, col = df.shape
    print()
    print(col, ' columns and ', row, ' records were loaded.')
    print()


# Define option 2 - View the data
def option2():
    print()
    print(df)
    print()


# List Departments and number of records
def option3():
    departments = df.groupby(['Department ']).size()
    print(departments)
    print()


# Search for Department records
def option4():
    print()
    user_dept = input('Please enter the department to see the records: ')
    print()
    print(user_dept)
    filtered = df.loc[df['Department '] == user_dept]
    # results = df.where(filtered)
    print(filtered.dropna(how='all'))
    # print(filtered)
    print()


def option5():
    max_net_sales = df['Net Sales'].max()
    print()
    sale_amt = int(input('Please enter lowest Net Sales you would like to see: '))
    print()
    max_net_sale = df[df['Net Sales'] > sale_amt]
    print()
    print('The largest net sale was ', max_net_sales)
    print()
    print('Records with Net Sales greater than ', sale_amt)
    print()
    print(max_net_sale)
    print()


def option6():
    print()
    search = input('Please enter the keyword to search for: ')
    print()
    auction_search = df[df['Auction Title '].str.contains(search, na=False)]
    print()
    print(auction_search)
    print()


def option7():
    print()
    dept_sales = df.groupby(['Department ']).sum()
    print()
    print(dept_sales)
    print()


def option8():
    print()
    search = int(input('Please enter the Auction ID to search for: '))
    print()
    auction_search = df[df['Auction ID'] == search]
    print()
    print(auction_search)
    print()


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            option8()
        elif option == 9:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')


