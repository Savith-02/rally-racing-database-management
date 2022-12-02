import re

print("\nSelect the option needed out of following: \n\
\tADD for adding driver details\n\
\tDDD for deleting\n\
\tUDD for updating driver details\n\
\tVCT for viewing the rally cross standings table\n\
\tSRR for simulating a random race\n\
\tVRL for viewing race table sorted according to the date\n\
\tSTF to save the current data to a text file\n\
\tRFF to load data from the saved text file\n\
\tESC to exit the program\n")


def ADD():  

    name = input("Enter name: ")
    for driver in drivers:
        if name == driver[0]:
            print("Driver exist. Enter another name or choose update option(UDD)")
            return
    
    age = input("Enter age: ")
    try:
        int(age)
    except:
        print("Invalid input")
        return
    team = input("Enter team: ")
    car = input("Enter car: ")
    current_points = input("Enter current points: ")
    try:
        float(current_points)
    except:
        print("Invalid input")
        return
    #data = [name, age, team, car, current_points]
    data = ", ".join([name, age, team, car, current_points])
    drivers.append([name, age, team, car, current_points])
    f = open('details.txt','a+')   
    #f.seek(0)
    f.writelines(data)
    f.write("\n")
    f.close()


def DDD():
    
    if len(drivers) == 0:
        print("No driver details for delete. Choose another option")
        return

    name_to_be_del = input("Enter driver name whose details neet to be deleted: ")

    f = open('details.txt','r')   
    all_lines = f.read()
    f.close()

    f = open('details.txt','w')   
    f.write(re.sub(name_to_be_del + ".*\s", "", all_lines))
    f.close()

    for driver in drivers:
        if name_to_be_del == driver[0]:
            drivers.remove(driver)
            return

    print("Driver doesnt exist. Enter another name or choose update option(UDD)")


def UDD():
    driver_to_be_updated = input("Enter driver name whose details neet to be updated: ")
    for driver in drivers:
        if driver_to_be_updated == driver[0]:
            drivers.remove(driver)
            return

def ESC():
    quit()

def PRT():
    max_length_of_data = [4, 3, 4, 3, 14]
    for driver in drivers:
        for i in range(5):
            no_of_characters = len(driver[i])
            if no_of_characters > max_length_of_data[i]:
                max_length_of_data[i] = no_of_characters

        """
        if len(driver[0]) > max_of_name:
            max_of_name = len(driver[0])
        if len(driver[1]) > max_of_age:
            max_of_age = len(driver[1])
        if len(driver[2]) > max_of_team:
            max_of_team = len(driver[2])
        """
    headers = ["name", "age", "team", "car", "current_points"]
    string = "_" * (sum(max_length_of_data) + 26) + "\n"
    for i in range(5):
        string += "|" + " " * (max_length_of_data[i] + 4)
    string += "|\n"
    for i in range(5):
        string += "|  " + headers[i] + " " * (max_length_of_data[i] + 2 - len(headers[i])) 
    string += "|\n"
    for i in range(5):
        string += "|" + "_" * (max_length_of_data[i] + 4)
    string += "|\n"
    for i in range(5):
        string += "|" + " " * (max_length_of_data[i] + 4)
    string += "|\n"
    for driver in drivers:
        for i in range(5):
            string += "|  " + driver[i]
            string += " " * (max_length_of_data[i] + 2 - len(driver[i]))
        string += "|\n"
    for i in range(5):
        string += "|" + "_" * (max_length_of_data[i] + 4)
    string += "|\n"
    print(string) 
 


Availabale_option = ["ADD", "DDD", "UDD", "RFF", "ESC", "PRT"]

try:
    f = open('details.txt','r')  
    drivers = []
    for line in f:
        driver = line.strip().split(", ")
        drivers.append(driver)
    f.close()
except:
    drivers = []


while(True):
    option = input("Enter option: ")

    if option in Availabale_option:
        locals()[option]()

