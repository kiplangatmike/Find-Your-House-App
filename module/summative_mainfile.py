from summative_users_parents_class import Agents
from summative_students_child_class import Students
import csv
import time

# ----------------------------------------------------------------------------------------------------------------------
# creating the objects of the Agents class
mike = Agents('Mike', 'Kip', 10, 1000, 123456)
natasha = Agents('natasha', 'Mramba', 20, 2000, 654321)

agents_list = []
# appending the agent object to the empty list above, the list will be used when storing the data into a csv file
agents_list.append(["Mike", "Kip",  10,  1000, 123456])
agents_list.append(["natasha", "Mramba", 20, 2000, 654321])

#---> wrote the data into a csv file
#---> commented out so that whn the programme id run again it cannot be written all over

# header = ["user_fname", "user_lname", "user_id", "user_pin", "user_phone_no"]
# with open("agents1.csv", "w+", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
#     writer.writerows(agents_list)
# ----------------------------------------------------------------------------------------------------------------------
# house is a list attribute that every agent has since they have houses
# when the houses is created, it is appended to the empty list of houses
house_list = []
house_list.append(natasha.add_house([natasha.user_id, 100, 3, 'kibaga', 300, 654321]))
house_list.append(natasha.add_house([natasha.user_id, 101, 2, 'mariot', 200, 654321]))
house_list.append(natasha.add_house([natasha.user_id, 102, 4, 'narito', 400, 654321]))
house_list.append(mike.add_house([mike.user_id, 200, 3, 'Remera', 300, 123456]))
house_list.append(mike.add_house([mike.user_id, 201, 3, 'kichukiro', 300, 123456]))
house_list.append(mike.add_house([mike.user_id, 202, 2, 'Lasve', 200, 123456]))
house_list.append(mike.add_house([mike.user_id, 203, 4, 'Nimro', 400, 123456]))

#---> wrote the data into a csv file
#---> commented out so that whn the programme id run again it cannot be written all over
header = ['Agent_id', 'house_id', 'room_no', 'location', 'price', 'agents_no']
with open("houses1.csv", "w+", newline="") as acsvfile:
    writer = csv.writer(acsvfile)
    writer.writerow(header)
    writer.writerows(house_list)
# ----------------------------------------------------------------------------------------------------------------------
# creating the objects of the Students class
jack = Students("jack", "Lumber", 30, 3000, 678901)
Marion = Students("marion", "Luke", 40, 4000, 234567)

students_list = []
# this objects are appended to the empty list so that it can be written to the csv file
students_list.append(["marion", "Luke", 40, 4000, 234567])
students_list.append(["jack", "Lumber", 30, 3000, 678901])

#---> wrote the data into a csv file
#---> commented out so that whn the programme id run again it cannot be written all over
# headercsv = ['user_fname', 'user_lname', 'user_id', 'user_pin', 'user_phone_no']
# with open("students1.csv", "w+", newline="") as acsvfile:
#     writer = csv.writer(acsvfile)
#     writer.writerow(headercsv)
#     writer.writerows(students_list)


# this is the main function with the whole code that runs the programme
def main():
    # this function is the first page that the user will interact with
    # the user will mention if he/she is a student or an agent
    # after that the user will be asked if he/she has an account
    # if he doesnt have an account, the function that allows him to create an account is called
    # if the user has an account, a function that lets him log into his account is called
    print("WELCOME TO FIND YOUR HOUSE\nThank you for choosing our platform to find your home")
    print("Are you a STUDENT or an AGENT?\n")
    print("Type 1 if you are an AGENT\nType 2 if you are a STUDENT")
    while True:
        user_input = input("ENTER:")
        # the if statements below is to direct the operation according to what the user wants to do
        if user_input == "1":
            print("\nDo you have an account?")
            print("Type 1 if YES\nType 2 if NO: ")
            user_input2 = input("ENTER: ")
            if user_input2 == "1":
                agent_login()
            if user_input2 == "2":
                agent_create_account()
        elif user_input == "2":
            print("do you have an account?")
            print("Type 1 if you have an account\n"
                  "Type 2 if you don't have an account")
            user_input3 = input("ENTER: ")
            if user_input3 == "1":
                student_login()
            if user_input3 == "2":
                student_create_account()
        else:
            print("wrong input, your input should be an integer.")


# this function allows the agent to log into the system
def agent_login():
    while True:
        try:
            # the user ID of the user is taken together with his/her pin
            account = int(input("Please enter your user_id: "))
            pin = int(input("please input your user_pin: "))
            print("Fetching data, please wait...\n")
            time.sleep(1)
            count = 0
            # the csv file that has the information of the agents is opened in read format
            # the input of the user which is the id and the pin is compared to the data that is in the csv file
            # if the information are the same the agent will be able to log into the system
            # if the information typed by the user would not correspond with the data in the csv file the agent will be
            # told that either the id or the pin is wrong and asked to check it once again

            with open("agents1.csv", "r") as acsvfile:
                reader = csv.DictReader(acsvfile)
                for row in reader:
                    if row['user_id'] == str(account) and row['user_pin'] == str(pin):
                        print(f'Hello {row["user_fname"]}, Welcome to FIND YOUR HOME')
                        count += 1
                        agent_task(account)
                if count == 0:
                    print("Account not found. Please ensure your user ID or user PIN is correct")
        except ValueError:
            print("wrong input, please input integers")


# this function allows the student to log into the system
def student_login():
    while True:
        try:
            # the user ID of the user is taken together with his/her pin
            account = int(input("Please enter your user_id: "))
            pin = int(input("please input your user_pin: "))
            print("Fetching data, please wait...\n")
            time.sleep(1)
            count = 0
            # the csv file that has the information of the students is opened in read format
            # the input of the user which is the id and the pin is compared to the data that is in the csv file
            # if the information are the same the agent will be able to log into the system
            # if the information typed by the user would not correspond with the data in the csv file the agent will be
            # told that either the id or the pin is wrong and asked to check it once again
            with open("students1.csv", "r") as acsvfile:
                reader = csv.DictReader(acsvfile)
                for row in reader:
                    if row['user_id'] == str(account) and row['user_pin'] == str(pin):
                        print(f'Hello {row["user_fname"]}, Welcome to FIND YOUR HOME')
                        count += 1
                        student_task(account)
                if count == 0:
                    print("You don't have an Account")
        except ValueError:
            print("wrong input, please input integers")


# this method allows creating an object for the agent class
def agent_create_account():
    while True:
        try:
            # all the attributes for the object is passed as user input
            while True:
                user_fname = input("input your first name: ").upper().strip()
                user_lname = input("input your second name: ").upper().strip()
                # the of statement checks if the input of the user is in letters
                # if it is not in letters it will prompt the user to input it in letters
                if user_fname.isalpha() and user_lname.isalpha():
                    print(user_fname, user_lname)
                    break
                else:
                    print("Your Names has to be in alphabets only.")
            user_id = int(input("input your national ID number: "))
            user_pin = int(input("input user_pin of your choice in integers:"))
            user_phone_no = int(input("input your phone number: "))
            print("Creating Account, please wait...\n")
            time.sleep(2)
            print(f"Welcome {user_fname}, your account has been created successfully.\n")
            # below the object of the agent is created and the user input is passed as arguements
            agent = Agents(user_fname, user_lname, user_id, user_pin, user_phone_no)
            # the attribute of the object created is passed into the the dictionary shown below as values
            # we are doing this so that we cound write it in the csv file
            new_agent_dict = {'user_fname': user_fname, 'user_lname': user_lname, 'user_id': user_id,
                              'user_pin': user_pin,
                              'user_phone_no': user_phone_no}
            header = ['user_fname', 'user_lname', 'user_id', 'user_pin', 'user_phone_no']
            from csv import DictWriter
            # we open the CSV file in append mode
            # Then, for the CSV file, create a file object
            with open('agents1.csv', 'a', newline='') as csvfile:
                # we passed the CSV  file object to the Dictwriter() function
                dictwriter_object = DictWriter(csvfile, fieldnames=header)
                # then pass the data in the dictionary as an argument into the writerow() function
                dictwriter_object.writerow(new_agent_dict)
                csvfile.close()
            agent_task(agent)

        except ValueError:
            print("wrong input, please input integers")


# this method allows creating an object for the student class
def student_create_account():
    while True:
        try:
            # all the attributes for the object is passed as user input
            while True:
                # the of statement checks if the input of the user is in letters
                # if it is not in letters it will prompt the user to input it in letters
                user_fname = input("input your first name: ").upper().strip()
                user_lname = input("input your second name: ").upper().strip()
                if user_fname.isalpha() and user_lname.isalpha():
                    break
                else:
                    print("Your Names has to be in alphabets only.")
            user_id = int(input("input your school ID number: "))
            user_pin = int(input("input user_pin of your choice in integers: "))
            user_phone_no = int(input("input your phone number: "))
            print("Creating Account, please wait...\n")
            time.sleep(2)
            print(f"Welcome {user_fname}, your account has been created successfully.\n")
            # below the object of the agent is created and the user input is passed as arguements
            user_info = Students(user_fname, user_lname, user_id, user_pin, user_phone_no)
            # the attribute of the object created is passed into the the dictionary shown below as values
            # we are doing this so that we could write it in the csv file
            new_student_dict = {}
            new_student_dict.update({'user_fname': user_fname, 'user_lname': user_lname, 'user_id': user_id, 'user_pin': user_pin,
                                    'user_phone_no': user_phone_no})
            header = ['user_fname', 'user_lname', 'user_id', 'user_pin', 'user_phone_no']
            from csv import DictWriter
            # we open the CSV file in append mode
            # Then, for the CSV file, create a file object
            with open('students1.csv', 'a', newline='') as csvfile:
                # we passed the CSV  file object to the Dictwriter() function
                dictwriter_object = DictWriter(csvfile, fieldnames=header)
                # then pass the data in the dictionary as an argument into the writerow() function
                dictwriter_object.writerow(new_student_dict)
                csvfile.close()
                student_task(user_info)
        except ValueError:
            print("wrong input, please input integers")


# this function is called after the agent has logged in or created an account
# this function contains the functions that the student can perform on the platform.
def agent_task(account):
    while True:
        try:
            # the print statements asks the user what he wants to do
            print("what would you like to do?")
            print("Type 1 to add house\n"
                  "Type 2 to to remove House\n"
                  "Type 3 to update House\n"
                  "Type 4 to view your house(s)\n"
                  "Type 5 to view your account details")
            # user types in what he wants to do below
            user_input1 = input("ENTER: ")
            if user_input1 == "1":
                # the inputs is taken from the user that will be used as the attributes when creating the house object
                house_id = int(input("What is the house id of the house you want to add?\nInput: "))
                no_rooms = int(input("What is the number of rooms in the house?\nInput: "))
                while True:
                    location = input("Where is the house located?\nInput: ").upper().strip()
                    # the if statement checks if the input of the location is in letters or not
                    if location.isalpha():
                        break
                    else:
                        print("Your Names has to be in alphabets only.")

                    price = int(input("What is the price of the house?\nInput: "))
                    agents_number = int(input("What is your phone number?\nInput: "))
                    agents_id = int(input("Enter your user id(national ID) for confirmation: "))
                    print(f"House with ID {house_id} that is in {location} has been added successfully ")
                    # an empty dictionary is created to store all the information of the house that will be
                    # used to write in the csv file
                    new_house_dict = {}
                    # we update the user input in the empty dictionary
                    new_house_dict.update({'agents_id': agents_id, 'house_id': house_id, 'room_no': no_rooms,
                                           'location':location, 'price': price, 'agents_no':agents_number})
                    header = ['agents_id', 'house_id', 'room_no', 'location', 'price', 'agents_no']
                    from csv import DictWriter
                    # we open the CSV file in append mode
                    # Then, for the CSV file, we create a file object
                    with open('houses1.csv', 'a', newline='') as csvfile:
                        # we pass the CSV  file object to the Dictwriter() function
                        dictwriter_object = DictWriter(csvfile, fieldnames=header)
                        dictwriter_object.writerow(new_house_dict)
                        csvfile.close()
                        agent_run_another_task(account)

            elif user_input1 == "2":
                user_ID = int(input("Enter your user ID for authentication: "))
                print("What is the house ID of the house you want to remove?")
                house_ID = int(input("ENTER House ID: "))
                Agents.remove_house(account, user_ID, house_ID)
                agent_run_another_task(account)
            elif user_input1 == "3":
                user_ID = int(input("Enter your user ID for authentication: "))
                print("what is the house ID of the house you want to update?")
                house_ID = int(input("ENTER House ID: "))
                Agents.update_house(account, user_ID, house_ID)

                agent_run_another_task(account)
            elif user_input1 == "4":
                # the user types in his id so that the houses that has that id that is typed will be printed to the user
                user_ID = int(input("Enter your user ID for authentication: "))
                Agents.get_house(account, user_ID)
                agent_run_another_task(account)

            elif user_input1 == "5":
                user_ID = input("please input your user_pin for verification: ")
                Agents.get_User_Info(account, user_ID)
                agent_run_another_task(account)

            else:
                print("Sorry wrong input, please select from the options")
        except ValueError:
            print("wrong input, please input integers")


# this function is called after a task has been finished by the agent to as him if he wants to run another task
def agent_run_another_task(account):
    while True:
        print("Do you want to do another task? \nType 1 if YES\nType 2 if NO")
        rerun = input("ENTER: ")
        if rerun == '1':
            # if the agent selects one it takes him back to the menu
            agent_task(account)
        elif rerun == '2':
            # if the agent selects 2, the programme exits
            print('Thank you for using our platform')
            exit()
        else:
            # if another key is typed by the agent, the following information is printed to the agent
            # this function is called once more to ensure that the agent inputs the correct input
            print('Wrong input! Please select from the given options')
            agent_run_another_task(account)


# this function is called after the student has logged in or created an account
# this function contains the functions that the student can perform on the platform.
def student_task(account):
    while True:
        print("MENU\nPress 1 to See your account\nPress 2 to see houses available")
        # the student is given the option to select the input according to the operation he wants
        user_input = input("ENTER: ")
        if user_input == "1":
            user_PIN = int(input("please input your USER ID for verification: "))
            # the method below is called from the student class if the student wants to see the his account info
            Students.get_User_Info(account, user_PIN)
            # then after the function below is called
            #  this function asks the student if he wants to perform another function
            student_run_another_task(account)
        elif user_input == "2":
            # if the student inputs 2 the getAllHouses is called
            # the geetAllHouses is a function that prints all the houses of the agents
            # from that the student can choose the house thaat he wants
            print("These are the houses available")
            getAllHouses()
            house_id = int(input("Enter the House ID of the house that you are renting \n Input: "))
            # after a student chooses a house, the csv file that contains the houses is opened in write mode
            # the house id that the student has entered is compared with the house ids in the csv file that has been opened
            file = open('houses1.csv', 'r')
            reader = csv.reader(file)
            # this list below will store the houses from the csv file
            list = []
            IfFound = False
            for row in reader:
                if row[1] == str(house_id):
                    IfFound = True
                else:
                    list.append(row)
            file.close()
            # if the house is not found, the student is notified that the his input was correct
            if IfFound == False:
                print('Invalid house id or user ID')
            else:
                # if the data is found, the csv is opened again, this time in write mode
                # the data is wrotten into the file without the house that the student has selected
                file = open('houses1.csv', 'w+', newline='')
                writer = csv.writer(file)
                writer.writerows(list)
            # the print output below is printed to show the student that the process has been successful
            print(f"You have rented house with ID {house_id}")
            student_run_another_task(account)
        else:
            print("Sorry wrong input, please select from the options")

# this function prints all the houses that are available in the csv file
def getAllHouses():
    # the csv file is opened and read
    with open("houses1.csv", "r") as acsvfile:
        reader = csv.reader(acsvfile)
        # there is a for loop that iterates through all the houses  and prints them as shown below
        for row in reader:
            print(f'House ID: {row[1]}, Number of rooms: {row[2]}, Price: {row[3]}, Agent_Number: {row[4]}')


# this method is called when a student has finished performing a certain task
# this function allows the student to run another task or terminate the process
def student_run_another_task(account):
    while True:
        print("Do you want to do another task? \nType 1 if YES\nType 2 if NO")
        rerun = input("ENTER: ")
        if rerun == '1':
            student_task(account)
        elif rerun == '2':
            print("Thank you for using our platform")
            exit()
        else:
            print('Wrong input! Please select from the given options')


main()

