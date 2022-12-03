#! /c/Python310/python
import random
import datetime

def ADD():
    name = str.upper(input("Enter name: "))
    global drivers
    for i in range(len(drivers)):
        if name == drivers[i][0]:
            print("Driver exist. Enter another name or choose update option(UDD)")
            return
    age = input("Enter age: ")
    try:
        int(age)
    except:
        print("Invalid input , Enter integers only")
        return

    team = input("Enter team: ")
    car = input("Enter car: ")
    current_points = input("Enter current points: ")
    try:
        int(current_points)
    except:
        print("Invalid input, Enter integers only.")
        return

    data = ", ".join([name, age, team, car, current_points])
    f = open('rally_details.txt', 'a+')
    f.write(data)
    f.write("\n")
    f.close()
    drivers.append([name, age, team, car, current_points])
    return drivers


def DDD():
    name_delete = str.upper(input("Enter driver name whose details need to be deleted : "))
    length_of_drivers_list = len(drivers)
    if length_of_drivers_list == 0:
        print("No driver details to delete. Choose add option (ADD)")
        return
    for driver1 in drivers:
        if name_delete == driver1[0]:
            drivers.remove(driver1)
            f = open('rally_details.txt', 'w')
            for line in drivers:
                f.write(", ".join(line))
                f.write("\n")
            f.close()
            #Changed break to return
            return

    #Added a print statement    
    print("No matching driver details.")
            


def UDD():
    global new_name
    length_of_drivers_list = len(drivers)
    if length_of_drivers_list == 0:
        print("No driver details to update. Choose add option (ADD) ")
        return
    name1 = str.upper(input("Enter driver name that need to be updated: "))
    for driver_list in drivers:
        if name1 == driver_list[0]:
            print("Current details:")
            print("\tname           ", ":", driver_list[0])
            print("\tage            ", ":", driver_list[1])
            print("\tteam           ", ":", driver_list[2])
            print("\tcar            ", ":", driver_list[3])
            print("\tcurrent points ", ":", driver_list[4])
            print("\nEnter which detail need to be updated :  \n\
                           \t 1 to update name\n\
                           \t 2 to update age\n\
                           \t 3 to update team\n\
                           \t 4 to update car \n\
                           \t 5 to update current points\n\
                           \t 6 to exit\n")
            
            index = drivers.index(driver_list)
            while True:
                update = int(input(" Enter 1,2,3,4,5,6: "))
                if update == 1:
                    new_name = str.upper(input("Enter new name :"))
                    drivers[index][0] = new_name

                elif update == 2:
                    new_age = input("Enter new age: ")
                    try:
                        int(new_age)
                    except:
                        print("Invalid input")
                        break
                    drivers[index][1] = new_age

                elif update == 3:
                    new_team = input("Enter new team: ")
                    drivers[index][2] = new_team

                elif update == 4:
                    new_car = input("Enter new car: ")
                    drivers[index][3] = new_car

                elif update == 5:
                    current_points1 = input("Enter new current points: ")
                    try:
                        int(current_points1)
                    except:
                        print("Invalid input")
                        break
                    drivers[index][4] = current_points1
                else:
                    break

            f = open('rally_details.txt', 'w')
            for line in drivers:
                f.write(", ".join(line))
                f.write("\n")
            f.close()
            return drivers

    print("No matching driver to update.")

    
def VCT():
    length = len(drivers)
    drivers_copy = drivers.copy()

    for x in range(0, length):
        for y in range(0, length-x-1):
            if int(drivers_copy[y][4]) < int(drivers_copy[y+1][4]):
                new = drivers_copy[y]
                drivers_copy[y] = drivers_copy[y+1]
                drivers_copy[y+1] = new

    max_length_of_data = [4, 3, 4, 3, 14]
    for driver in drivers_copy:
        for i in range(5):
            no_of_characters = len(driver[i])
            if no_of_characters > max_length_of_data[i]:
                max_length_of_data[i] = no_of_characters

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
    for driver in drivers_copy:
        for i in range(5):
            string += "|  " + driver[i]
            string += " " * (max_length_of_data[i] + 2 - len(driver[i]))
        string += "|\n"
    for i in range(5):
        string += "|" + "_" * (max_length_of_data[i] + 4)
    string += "|\n"
    print(string)


def SRR():
    c = open('race_locations.txt', 'r')
    location =[]
    for locations in c :
        # removes split()
        place = locations.strip()
        location.append(place)
    c.close()
    random_location = random.choice(location)

    # ADDED the datetime.data.isoformat()
    # https://www.geeksforgeeks.org/python-datetime-module/
    x = datetime.date.isoformat(datetime.date(year=2022, month=random.randint(1, 12), day=random.randint(1, 30)))
    
    print("DATE : ",x)
    print("LOCATION :", random_location)

    race = []
    race.append(x)
    race.append(random_location)
    
    name_list = []
    for name in drivers:
        name_list.append(name[0])

    size = len(name_list) + 1
    # removed the while loop
    for i in range(1, size):
        random_name = random.choice(name_list)
        name_list.remove(random_name)
        print(i , ":", random_name )
        race.append(random_name)

    place_points = {
        1: 10,
        2: 7,
        3: 5
    }
    for i in range(2,5):
        for j in range(len(drivers)):
            if drivers[j][0] == race[i]:
                drivers[j][4] = str(int(drivers[j][4]) + place_points[i-1])
                break
            
    f = open('race_details.txt', 'a+')
    data = ", ".join(race)
    f.write(data)
    f.write("\n")
    f.close()


def ESC():
    print("END")
    quit()


print("\t~~~ WORLD RALLY CROSS CHAMPIONSHIP ~~~")

print("\nType the option : \n\
\tADD for adding driver details\n\
\tDDD for deleting\n\
\tUDD for updating driver details\n\
\tVCT for viewing the rally cross standings table\n\
\tSRR for simulating a random race\n\
\tVRL for viewing race table sorted according to the date\n\
\tSTF to save the current data to a text file\n\
\tRFF to load data from the saved text file\n\
\tESC to exit the program\n")

try:
    f = open("rally_details.txt", 'r')
    drivers = []
    for line in f:
        driver = line.strip().split(", ")
        drivers.append(driver)
    f.close()
except:
    drivers = []
    
    
while (True):
    option = str.upper(input("\nEnter the option :"))
    Availabale_option = ["ADD", "DDD", "UDD","VCT","SRR", "RFF", "ESC"]
    if option in Availabale_option:
        locals()[option]()
    else:
        print("invalid option")

