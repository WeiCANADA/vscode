import csv
""" with open('data.csv', 'r') as csv_file:
    #csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader
    for line in csv_reader:
        print(line) """
def add_user(first_name,last_name):
    with open('users.csv','r+',newline='') as csvfile:
        userwriter = csv.writer(csvfile,delimiter = ',')
        userwriter.writerow([first_name] + [last_name])

add_user('Darth2','Vader')
