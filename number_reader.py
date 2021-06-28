from os import name, write
import re

phone_number_list = []

print("Welcome to the Phone-Number Reader")

#accept input from the user for a file path
file_path = input(f"Please enter the path to the file you would like read: ")
filename = file_path

#accept input from the user for the location of the new file location
new_file_path = input(f"Please enter the path where you would like the final file to go: ")
new_filename = new_file_path

#open the file in the specified location
with open(filename) as f:
    content = f.readlines()

#read reach line of the opened file which we saved to content.
for line in content:
    #This is the regular expression style I am looking for in this case a phone number
    phone_numbers_search = re.compile(r"\d{3}-\d{3}-\d{4}")

    #This saves the phone numbers that are found into a list format (mo means match object)
    mo = phone_numbers_search.findall(line)

    #Append the phone number value to the final phone list
    for number in mo:
        phone_number_list.append(number)

#Converts the list that was generated into a string and creates a file with it.
with open(new_filename, "w") as f:
    f.write(str(phone_number_list))



    