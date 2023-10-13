# steve github

# from dev2

def house_cleaning():
    #Types of cleaning initialization, Here we are offering three types of cleaning
    floors = 100
    windows = 50
    dusting = 80

    #Initializing a variable total to calculate the cost of cleaning
    total = 0

    #Size of houses prices initialization, As they are initialized with 1, 2, and 4 beacause according to the size of the house we will be multiplying the cleaning type to compute the total cost in the end for cleaning
    small = 1
    medium = 2
    large = 4

    #Taking input from the user of type of cleaning and size of the house
    type_cleaning = input("Please Enter the type of cleaning you want(floors, windows, or dusting):")
    size = input("Please Enter the size of house you want cleaned(small, medium, or large):")

    #Using if-else structure to calculate the cost of the cleaning if the size is small and for different type of cleaning using nested if-else, As using that we will be able to differentiate different type of cleaning
    if size == 'small':
        if type_cleaning == 'floors':
            total = floors * small
        elif type_cleaning == 'windows':
            total = windows * small
        elif type_cleaning == 'dusting':
            total = dusting * small

    #Using if-else structure to calculate the cost of the cleaning if the size is medium and for different type of cleaning using nested if-else,
    elif size == 'medium':
        if type_cleaning == 'floors':
            total = floors * medium
        elif type_cleaning == 'windows':
            total = windows * medium
        elif type_cleaning == 'dusting':
            total = dusting * medium

    #Using if-else structure to calculate the cost of the cleaning if the size is large and for different type of cleaning using nested if-else,
    elif size == 'large':
        if type_cleaning == 'floors':
            total = floors * large
        elif type_cleaning == 'windows':
            total = windows * large
        elif type_cleaning == 'dusting':
            total = dusting * large

    #Printing the total cost on the screen
    return total

def yard_service():

    # initializing values for mowing, edging, shrub
    mowing = 5
    edging= 10
    shrub = 3

    #intializing total cost to calculate total
    total = 0

    # prompting user for input of type of service
    type_service = input("Please Enter the type of service you want(mowing, edging, or shrub):").upper()

    # using if elif statement and calculating the cost
    if type_service == 'MOWING':
        square_foot = int(input('Please enter the square footage of the yard: '))
        total = square_foot * mowing
    elif type_service == 'EDGING':
        linear_foot = int(input("Please enter linear footage of the yard: "))
        total = edging
    elif type_service == 'SHRUB':
        shrub_number = int(input("Pleaseenter number of shrubs: "))
        total= shrub * shrub_number

    # returning the total
    return total

# function to calculate discount
def discount(cost, percent):
    return cost * (cost -percent / 100)

# promting user whether they want to use House cleaning or Yard service
service_type = input("Enter 'HC' for House cleaning service, 'YS' for Yard service: ").upper()

# using while loop to loop until unser enter correct input
while  service_type != 'HC' and service_type != 'YS':
    service_type = input("Please enter correct input. Enter 'HC' for House cleaning service, 'YS' for Yard service: ").upper()

# prompting user for input whether they are senior citizon or not
is_senior = input("Are you a senior citizen? Yes or No: ").upper()

# setting the discount percentage, currently set as 10
senior_discount_percent = 10

# checking the input and accepting if the input is either yes or no
while  is_senior != 'YES' and is_senior != 'NO':

    # prompting text to take input
    is_senior = input("Please enter correct input. Are you a senior citizen? Yes or No: ").upper()

# checking the type of service
if service_type == 'HC':

    # if input is HC then we call house_cleaning function
    cost = house_cleaning()
else:

    # if input is HC then we call yard_service function
    cost = yard_service()

# checking whether user is senior or not
if is_senior == 'YES':

    # giving discount if above condition satisfies
    cost = discount(cost, senior_discount_percent)

# printing the final cost
print("Total cost for the service is: " ,cost)
