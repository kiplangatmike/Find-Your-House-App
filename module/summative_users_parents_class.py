# this is the parent class that has all the attributes to be inherited by the child classes.
import csv
class Users:
    def __init__(self, fname='', lname='', user_id='', user_pin='',  phone_no=''):
        self.fname = fname  # first name
        self.lname = lname  # last name
        self.user_id = user_id  # unique identifier for the user
        self.user_pin = user_pin  # unique password for each user
        self.phone_no = phone_no  # contact of the user

# using this class we will be creating objects of the agents that will be using this platform
# this class inherits its attributes from the User class


class Agents(Users):
    # in this constructor we initialize the attributes that the agent will we having and use the super innit to inherit
    def __init__(self, fname='', lname='', user_id='', user_pin='', phone_no=''):
        super().__init__(fname, lname, user_id, user_pin, phone_no)
        self.houses = []

# this method returns the houses for a particular agent that is stored in the self.houses
    def get_house(self, user_ID):
        # this variable count is created so that if that particular id is not found the user will be told that he
        # doesnt have a house, it will remain zero but if it is found  +=1
        found = 0
        count = 0
        with open("houses1.csv", "r") as acsvfile:
            reader = csv.DictReader(acsvfile)
            # the for loop iterates through the file checking if the agent's id in the file is the same as the the id
            # that is provided, if it finds the id that are similar, the houses with those ids will be printed
            for row in reader:
                if row['Agent_id'] == str(user_ID):
                    count += 1
                    found = +1
                    print(
                        f"House ID: {row['house_id']}, Number of rooms: {row['room_no']}, Location: {row['location']},"
                        f" Price: {row['price']}, Your Phone Number: {row['agents_no']}")

            if found == 0:
                print("You don't have any house")
        return found

# this is a method that allows an agent to add a house and pass all the attributes of the house
    def add_house(self, house_id='', no_rooms='', location='', price='', agents_number=''):
        house_data = [house_id, no_rooms, location,  price, agents_number]
        # this house created is updated to the dictionary created for the agent
        self.houses = (house_data)
        return self.houses[0]

# this method allows the agent to remove a house, the agent provides the house id which is the key in the dictionary
    def remove_house(self, user_ID, house_ID):
        # we need to access the houses that we stored in the csv file
        # we first open the file in read mode
        result = 1
        file = open('houses1.csv', 'r')
        reader = csv.reader(file)
        # we create an empty list that will hold the houses temporarily
        list = []
        # we take the user ID and the house id which the user wants to remove, this will be used in comparing
        # the user input with the information that is in the csv file. if the information corresponds the house will
        # be removed from the csv file to the empty list
        # this if found variable is used to indicate if the the data is in the csv file or not
        IfFound = False
        for row in reader:
            if row[1] == str(house_ID) and row[0] == str(user_ID):
                IfFound = True
                #result= 1
                print(f"you have successfully removed house with ID: {house_ID}")
            else:
                list.append(row)
        file.close()

        # IfFound remains false that means that the information was not found and the print statement below is printed
        if IfFound == False:
            print('Invalid house id or user ID')

        else:  # if it is found the the file is opened again and written with the information that remained in the list
            # after the house has been removed

            file = open('houses1.csv', 'w+', newline='')
            writer = csv.writer(file)
            writer.writerows(list)
        file.close()
        return IfFound


# this method is for the agent to update the price of the house and his number if he/she changes it
    def update_house(self, user_ID, house_ID):
        print('Type 1 to update Price\nType 2 to update your phone number')
        # the agent picks that he/she wants to update
        toUpdate = input("ENTER: ")
        # the user ID is also provided for comparison purposes between the input of the user and if the data is there
        # in the csv file that is being accessed by the agent
        #user_ID = int(input("Enter your user ID for authentication: "))
        # if the input of the user above was to update the price of the house ot brings him here
        if toUpdate == '1':

            # the user has to enter the house id of the house that he wants to update
            #house_id = int(input("ENTER House ID: "))
            # the csv file is opened
            file = open('houses1.csv', 'r')
            reader = csv.reader(file)
            # we create an empty list where we will store the data form the csv temporarily
            list = []
            # we will also take the id of the user to make sure that the agent id and the house id matches
            # so that the no other person can update the house
            # the IfFound variable indicated if the data is there in the csv file or not
            IfFound = False
            # the for loop iterates over the data to check if the data is there
            for row in reader:
                if row[1] == str(house_ID) and row[0] == str(user_ID):
                    # if the data that matches is both in the csv file and the user input, the variable that
                    # we had changes to True
                    IfFound = True
                    # since the data is found, we create a variable that asks the what is the new price of the house
                    new_Price = input("Enter New Price: ")
                    # the price element is the forth on the list, so we access the element in the list as shown below
                    row[4] = new_Price
                # we then append the record then close it
                list.append(row)
            file.close()
            if IfFound == False:
                print('Invalid house id or user ID')
            else:
                file = open('houses1.csv', 'w+', newline='')
                writer = csv.writer(file)
                writer.writerows(list)
                file.close()
                return IfFound
        elif toUpdate == '2':
            # the csv file is opened
            file = open('houses1.csv', 'r')
            reader = csv.reader(file)
            # we create an empty list where we will store the data form the csv temporarily
            list = []
            # we will also take the id of the user to make sure that the agent id and the house id matches
            # so that the no other person can update the house
            # the IfFound variable indicated if the data is there in the csv file or not
            IfFound = False
            for row in reader:
                # the for loop iterates over the data to check if the data is there
                if row[0] == str(user_ID):
                    # if the data that matches is both in the csv file and the user input, the variable that
                    # we had changes to True
                    IfFound = True
                    # since the data is found, we create a variable that asks the what is the new price of the house
                    new_Number = input("Enter New Number: ")
                    # the number element is the fifth on the list, so we access the element in the list as shown below
                    row[5] = new_Number
                    # we then append the record then close it
                list.append(row)
            file.close()
            # if data is not found  the statement below is printed
            if IfFound == False:
                print('Invalid user ID or check if you have houses')
            else:
                # if the house is found,  the file is opened again and the information that eas updated is
                # updated to the csv file
                file = open('houses1.csv', 'w+', newline='')
                writer = csv.writer(file)
                writer.writerows(list)
            file.close()
            return IfFound
        else:
            print("Wrong input")


    # this method is for displaying the information of agent, it fetches the data from teh csv file that stored the
    # objects of agents when they were being created
    def get_User_Info(self, user_PIN):
        # we are taking the id so that we can fetch the information of that particular agent

        count = 0
        # the csv file is opened in read mode since we just want to view the information
        found = 0
        with open("agents1.csv", "r") as acsvfile:
            reader = csv.DictReader(acsvfile)
            # the for loop iterates over the data
            for row in reader:
                # if data in the cv matches that of agents input, the information of the agent is printed
                if row['user_pin'] == str(user_PIN):
                    found = 1
                    print(f"Your info:\nuser_id:{row['user_id']}\nfirst_name:{row['user_fname']}\nlname:{row['user_lname']}\nphone_no:{row['user_phone_no']}")
                    count += 1
            if found == 0:
                print("Your user ID is incorrect, check your user ID")
        return found
