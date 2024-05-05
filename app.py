import random
import datetime
def ADD():
    f = open('rally_details.txt', 'a+')
    f.seek(0)
    name = str.upper(input("Enter name: "))
    global drivers
    for i in range(len(drivers)):
        if name in drivers[i]:
            print("Driver exist. Enter another name or choose update option(UDD)")
            return
    age = input("Enter age: ")
    try:
        int(age)
    except:
        print("Invalid input , Enter integers only")
        return

    team = str.upper(input("Enter team: "))
    car = str.upper(input("Enter car: "))
    current_points = input("Enter current points: ")
    try:
        int(current_points)
    except:
        print("Invalid input, Enter integers only")
        return


    data = ", ".join([name, age, team, car, current_points])
    f.writelines(data)
    f.write("\n")
    f.close()
    drivers.append([name, age, team, car, current_points])
    return drivers


def DDD():
    name_delete = str.upper(input("Enter driver name whose details need to be deleted : "))
    length_of_drivers_list = len(drivers)
    if length_of_drivers_list == 0:
        print("No driver details to delete. Choose add option (ADD) ")
        return
    for driver1 in drivers:
        if name_delete == driver1[0]:
            drivers.remove(driver1)
            f = open('rally_details.txt', 'w')
            for line in drivers:
                f.writelines(", ".join(line))
                f.write("\n")
            f.close()
            break
        #else:
            #print("No matching driver details  ")
            #DDD()


def UDD():
    global new_name
    length_of_drivers_list = len(drivers)
    if length_of_drivers_list == 0:
        print("No driver details to update  . choose add option (ADD) ")
        return
    name1 = str.upper(input("Enter driver name that need to be updated : "))
    for driver_list in drivers:
        if name1 == driver_list[0]:
            print("name           ", ":", driver_list[0])
            print("age            ", ":", driver_list[1])
            print("team           ", ":", driver_list[2])
            print("car            ", ":", driver_list[3])
            print("current points ", ":", driver_list[4])
            print("\nEnter which detail need to be updated :  \n\
                           \t 1 to update name\n\
                           \t 2 to update age\n\
                           \t 3 to update team\n\
                           \t 4 to update car \n\
                           \t 5 to update current points\n\
                           \t 6 to exit\n")
        #else:
           # print("No matching driver to update ")


    while True:
        update = int(input(" Enter 1,2,3,4,5,6 : "))
        if update == 1:
            new_name = str.upper(input("Enter new name :"))
            name1 = new_name
            for driver1 in drivers:
                if name1 == driver1[0]:
                    driver1[0] = new_name
                    return new_name

        elif update == 2:
            age1 = input("Enter new age: ")
            try:
                int(age1)
            except:
                print("Invalid input")
                age1 = input("Enter new age: ")
            for driver1 in drivers:
                if name1 == driver1[0]:
                    driver1[1] = age1


        elif update == 3:
            team1 = str.upper(input("Enter new  team: "))
            for driver1 in drivers:
                if name1 == driver1[0]:
                    driver1[2] = team1

        elif update == 4:
            car1 = str.upper(input("Enter car: "))
            for driver1 in drivers:
                if name1 == driver1[0]:
                    driver1[3] = car1
        elif update == 5:
            current_points1 = input("Enter new  current points: ")
            try:
                int(current_points1)
            except:
                print("Invalid input")
                return
            for driver1 in drivers:
                if name1 == driver1[0]:
                    driver1[4] = current_points1
        else:
            break
    f = open('rally_details.txt', 'w')
    for line in drivers:
        f.writelines(", ".join(line))
        f.write("\n")
    f.close()
    return drivers

def VCT():
    length = len(drivers)
    for x in range(0,length):
        for y in range(0,length-x-1):
            if drivers[y][4] < drivers[y+1][4]:
                new = drivers[y]
                drivers[y] = drivers[y+1]
                drivers[y+1] = new
    max_length_of_data = [4, 3, 4, 3, 14]
    for driver in drivers:
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
    for driver in drivers:
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
    race = []
    location =[]
    name_list = []
    x = datetime.date(year=2022, month=random.randint(1, 12), day=random.randint(1, 30))
    for locations in c :
        place = locations.strip().split(", ")
        location.append(place)
    f.close()
    for name in drivers:
        name_list.append(name[0])
    random_location = random.choice(location)
    print("DATE : ",x)
    print("LOCATION :", random_location)
    race.append(x)
    race.append(random_location)
    size = len(name_list)+1
    while len(name_list) > 0:
        for i in range(1,size):
            random_name = random.choice(name_list)
            name_list.remove(random_name)
            print(i , ":", random_name )
            race.append(random_name)
    for driver in drivers:
        if race[2]== driver[0]:
            driver[4]= driver[4]+10








def ESC():
    print("END")
    quit()

print("\tWORLD RALLY CROSS CHAMPIONSHIP ")

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
    option = str.upper(input("Enter the option :"))
    Availabale_option = ["ADD", "DDD", "UDD","VCT","SRR", "RFF", "ESC"]
    if option in Availabale_option:
        locals()[option]()
    else:
        print("invalid option)
