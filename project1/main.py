import csv
import random
import datetime


product = ('Brozne', 'Silver', 'Gold')
first_name = ('John', 'andy', 'Dave', 'Bob', 'Wilbur', 'Joe')
last_name = ('Smith', 'William', 'Hicks')
postcodes = ('Bh15 2EX', 'BH12 2NG', 'BH13 7BB')
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(20)]


num = int(input("How many records would you like:"))



header = ['Product', 'Policyholder Name',
          'Number of people covered', 'postcodes', 'Start date of policy']


with open('testdata.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    writer.writerow(header)

    
    for n in range(num):
        data = [random.choice(product), random.choice(
            first_name) + " " + random.choice(last_name), random.randint(1,10), random.choice(postcodes), random.choice(date_list)]
        writer.writerow(data)
