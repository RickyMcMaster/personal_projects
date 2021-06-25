# from csv import DictReader, reader, reader
import itertools
import csv

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

# fp = "colt_steele/python_bootcamp/"


def add_user(first, last):
    data = [first, last]
    with open("users.csv", "a") as f:
        reader = csv.reader(f)
        reader.readerow(data)


# add_user("Dwayne", "Johnson")  # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson


def print_users():
    with open("users.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            # print(row)
            print("{} {}".format(row['First Name'], row['Last Name']))


# print_users()

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''


def find_user(first, last):
    with open("users.csv") as f:
        csv_reader = csv.reader(f)
        for count, row in enumerate(csv_reader):
            if row[0] == first and row[1] == last:
                return count
        return "Not Here not found."


# print(find_user("Karg", "Steele"))


def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as f:
        csv_reader = csv.reader(f)
        counter = 0
        update_list = []
        for row in csv_reader:
            if row[0] == old_first and row[1] == old_last:
                update_list.append([new_first, new_last])
                counter += 1
            else:
                update_list.append([row[0], row[1]])
    with open('users.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for u in update_list:
            csv_writer.writerow(u)
    return "Users updated: {}.".format(counter)


# print(update_users("Grace", "Hopper", "Hello", "World"))  # Users updated: 1.
# print(update_users("Colt", "Steele", "Boba", "Fett"))  # Users updated: 2.
# print(update_users("Not", "Here", "Still not", "Here"))  # Users updated: 0.


def delete_users(old_first, old_last):
    with open("users.csv") as f:
        csv_reader = csv.reader(f)
        counter = 0
        update_list = list(csv_reader)
        for elem, row in enumerate(update_list):
            if row[0] == old_first and row[1] == old_last:
                update_list.pop(elem)
                counter += 1
        # print(update_list)
    with open('users.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for u in update_list:
            csv_writer.writerow(u)
    return "Users deleted: {}.".format(counter)

# Colt's solution - more efficient
def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)


print(delete_users("Grace", "Hopper"))  # Users deleted: 1.
print(delete_users("Colt", "Steele"))  # Users deleted: 2.
print(delete_users("Not", "Here"))  # Users deleted: 0.
