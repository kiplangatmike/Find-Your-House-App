# we import the Agents since we are inheriting its methods and attributes.
from summative_users_parents_class import Agents
# we import csv so that we can read the csv files when getting data of the users
import csv

# this class is for creating objects of the students
class Students(Agents):
    def __init__(self, fname='', lname='', user_id='', user_pin='', phone_no=''):
        # all the attributes are inherited from the agents class thus the use of super __init__
        super().__init__(fname, lname, user_id, user_pin, phone_no)

    # this method gets the details of the user from the csv file where the data is stored permanently
    def get_User_Info(self, user_ID):
        # the user_Pin is used to fetch the data for the student as it compares it with the the the column of id of the
        # user in the csv file

        count = 0
        # the csv file is opened
        found = 0
        with open("students1.csv", "r") as acsvfile:
            reader = csv.DictReader(acsvfile)
            for row in reader:
                if row['user_id'] == str(user_ID):
                    found = 1
                    print(
                        f"Your info:\nuser_id:{row['user_id']}\nfirst_name:{row['user_fname']}\nlname:{row['user_lname']}\nphone_no:{row['user_phone_no']}")
                    count += 1
            if found == 0:
                 print("Your user ID is incorrect, check your user ID")

        return found
